import ollama  # Para generar respuestas con el modelo de lenguaje
import threading  # Para mostrar "Pensando..."
import time  # Para pausas en la animación
import mysql.connector as mysql  # Para almacenar historial de conversación
import os

# =========================
# CONEXIÓN A BASE DE DATOS
# =========================
import mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        host="localhost",
        user="root",  # Cambia si usas otro usuario
        password="Contraseña",  # Cambia por tu contraseña de MySQL
        database="chat_historial",  # NUEVO nombre de la base de datos
        auth_plugin="mysql_native_password",
        charset="utf8mb4"
    )


def guardar_mensaje(usuario, personaje, mensaje):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO historial_chat (usuario, personaje, mensaje) VALUES (%s, %s, %s)", (usuario, personaje, mensaje))
        conexion.commit()
    except mysql.Error as err:
        print(f"❌ Error al guardar el mensaje: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()

def ver_historial():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT usuario, personaje, mensaje FROM historial_chat ORDER BY id DESC LIMIT 10;")
        historial = cursor.fetchall()
        print("\n📜 Historial de Chat:")
        for usuario, personaje, mensaje in historial:
            print(f"{usuario} ({personaje}): {mensaje}")
    except mysql.Error as err:
        print(f"❌ Error al recuperar historial: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()

# =========================
# CHATBOT DE PERSONAJES HISTÓRICOS
# =========================

def mostrar_pensando():
    for _ in range(3):
        for dots in range(1, 4):
            print(f"🤖 Pensando{'.' * dots}", end="\r")
            time.sleep(0.5)

def chat_con_personaje():
    print("🤖 Chatbot con Personajes Históricos")
    print("Elige un personaje para conversar:")
    personajes = {
        "1": "Albert Einstein",
        "2": "Nikola Tesla",
        "3": "Leonardo da Vinci",
        "4": "Isaac Newton",
        "5": "Cleopatra",
    }
    
    for key, value in personajes.items():
        print(f"{key}. {value}")
    
    opcion = input("Selecciona el número del personaje: ").strip()
    personaje = personajes.get(opcion, "Albert Einstein")
    print(f"✅ Has elegido conversar con {personaje}.\n")
    
    print("Escribe 'salir' para terminar o 'historial' para ver el historial.")
    
    while True:
        pregunta = input("Tú: ").strip()
        
        if pregunta.lower() == "salir":
            print("🔚 Chat finalizado.")
            break
        
        elif pregunta.lower() == "historial":
            ver_historial()
            continue
        
        guardar_mensaje("Usuario", personaje, pregunta)
        
        hilo_pensando = threading.Thread(target=mostrar_pensando)
        hilo_pensando.start()
        
        # Construcción del mensaje para el modelo
        mensajes = [
            {"role": "system", "content": f"Eres {personaje}, responde como lo haría él en español."},
            {"role": "user", "content": pregunta}
        ]
        
        respuesta = ollama.chat(
            model="deepseek-r1:7b",  # Puedes cambiar el modelo aquí
            messages=mensajes
        )
        
        hilo_pensando.join()
        mensaje_respuesta = respuesta['message']['content']
        print(" " * 20, end="\r")  # Limpiar la animación
        print(f"🤖 {personaje}: {mensaje_respuesta}")
        
        guardar_mensaje(personaje, "Usuario", mensaje_respuesta)

if __name__ == "__main__":
    chat_con_personaje()
