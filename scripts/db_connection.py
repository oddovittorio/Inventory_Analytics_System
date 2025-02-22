import mysql.connector
from dotenv import load_dotenv
import os

#.env Datei laden
load_dotenv()

# Verbindung zu MySQL herstellen mit Werten aus .env Datei
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)