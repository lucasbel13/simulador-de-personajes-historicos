🤖 Chatbot de Personajes Históricos

📌 Descripción

Este es un chatbot interactivo que permite conversar con personajes históricos como Albert Einstein, Nikola Tesla, Leonardo da Vinci, Isaac Newton y Cleopatra.

El chatbot genera respuestas utilizando Ollama y almacena el historial de conversación en MySQL.

🚀 Características

✅ Interacción con personajes históricos.✅ Elección del personaje antes de iniciar la conversación.✅ Respuestas generadas con IA (Ollama) basadas en el estilo del personaje.✅ Almacenamiento del historial en MySQL.✅ Recuperación del historial de conversaciones.✅ Animación de "Pensando..." mientras se genera la respuesta.

📂 Instalación y Configuración

1️⃣ Requisitos Previos

Python 3.8+

MySQL Server instalado y corriendo

Tener instalado pip

Tener configurado Ollama en tu máquina

2️⃣ Instalar las Dependencias

Ejecuta el siguiente comando en la terminal:

pip install mysql-connector-python ollama

3️⃣ Crear la Base de Datos en MySQL

Ejecuta el siguiente código en MySQL para crear la base de datos y la tabla:

CREATE DATABASE chat_historial CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE chat_historial;

CREATE TABLE historial_chat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    personaje VARCHAR(255) NOT NULL,
    mensaje TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

4️⃣ Configurar la Conexión a MySQL

Edita el archivo chatbot_personajes.py y asegúrate de cambiar las credenciales de MySQL en la función conectar_db():

import mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        host="localhost",
        user="root",  # Cambia si usas otro usuario
        password="Contraseña",  # Cambia por tu contraseña
        database="chat_historial",
        auth_plugin="mysql_native_password",
        charset="utf8mb4"
    )

🎮 Uso del Chatbot

Ejecuta el script principal:

python chatbot_personajes.py

💡 Comandos disponibles:

Escribe tu pregunta para interactuar con el personaje.

Escribe "salir" para terminar la conversación.

Escribe "historial" para ver las últimas conversaciones guardadas.

🛠️ Mejoras Futuras

✅ Agregar más personajes históricos.✅ Mejorar la personalización de las respuestas.✅ Implementar una interfaz gráfica (GUI).✅ Integración con una API web para acceso desde navegadores.

Si tienes alguna sugerencia, ¡colabora en el repositorio! 🎉
