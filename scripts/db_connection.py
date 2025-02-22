import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

#.env Datei laden
load_dotenv()

def get_sales_data():
  # Verbindung zu MySQL herstellen mit Werten aus .env Datei
  with mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
    ) as conn:
    # SQL-Abfrage definieren
    query = "SELECT * FROM sales;"  # Holt alle Zeilen aus der sales-Tabelle
    # Daten aus MySQL in einen Pandas DataFrame laden
    df = pd.read_sql(query, conn)
  return df
  
  
  