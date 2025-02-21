import csv, uuid, random
from faker import Faker

fake = Faker() #Faker-Objekt erstellen
rand = random.Random() #Random-Objekt erstellen

#Liste mit realisitischen Sneakrs-Produkten
sneakrs_products = [
    "Nike Air Force 1",
    "Nike Dunk Low",
    "Nike Air Max 90",
    "Nike Air Jordan 1 Retro",
    "Nike Blazer Mid '77",
    "Nike SB Dunk High",
    "Nike ZoomX Vaporfly Next%",
    
    "Adidas Yeezy Boost 350",
    "Adidas Yeezy 700",
    "Adidas Ultra Boost",
    "Adidas Samba OG",
    "Adidas NMD R1",
    "Adidas Superstar",
    "Adidas Forum Low",
    
    "New Balance 550",
    "New Balance 2002R",
    "New Balance 990v5",
    "New Balance 327",
    
    "Puma RS-X",
    "Puma Suede Classic",
    "Puma Future Rider",
    
    "Reebok Club C 85",
    "Reebok Classic Leather",
    
    "Converse Chuck Taylor All Star",
    "Converse Run Star Hike",
    
    "Vans Old Skool",
    "Vans Sk8-Hi",
    
    "Asics Gel-Lyte III",
    "Asics Gel-Kayano 14",
    
    "Salomon XT-6",
    "Salomon Speedcross 5"
]

# Datei öffnen und schreiben
with open("data/sneakrs_sales.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Spaltennamen schreiben  
    writer.writerow(["order_id","customer_name","product","size","price_per_unit","total_price","quantity","order_date"])
    
    # 1000 Verkaufsdatensätze generieren
    for i in range(1000):
      order_id = uuid.uuid4()
      customer_name = fake.name()
      product = rand.choice(sneakrs_products)
      size = rand.randint(36, 47)
      price_per_unit = rand.randint(100, 500)
      quantity = rand.randint(1, 5)
      total_price = price_per_unit * quantity
      order_date = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
      
      writer.writerow([order_id, customer_name, product, size, price_per_unit, total_price, quantity, order_date])