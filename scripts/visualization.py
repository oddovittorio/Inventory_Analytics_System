import matplotlib.pyplot as plt
from db_connection import get_sales_data

# Verkaufsdaten aus der Datenbank abrufen -> visualization.py mit db_connection.py verknüpfen
df = get_sales_data()

# Einfaches leeres Diagramm erstellen
plt.figure(figsize=(6, 4))  # Größe des Diagramms festlegen
plt.title("Erstes Matplotlib Diagramm")  # Titel setzen

# Diagramm anzeigen
plt.show()