stock = [ ["Laptop", 15, 1200.50],
    ["Mouse", 50, 25.99],
    ["Keyboard", 30, 45.00],
    ["Monitor", 20, 220.75],
    ["USB Cable", 100, 5.50],
    ["Headphones", 25, 75.20],
    ["Webcam", 10, 60.00],
    ["External HDD", 12, 110.00],
    ["Smartphone", 18, 800.99],
    ["Charger", 40, 18.75]]  
# each product = ["name", quantity, unit_price]

# stock.py
def add_product(stock, name, quantity, price):
    stock.append([name, quantity, price])

def remove_product(stock, name):
    stock[:] = [p for p in stock if p[0] != name]

def update_quantity(stock, name, quantity):
    for p in stock:
        if p[0] == name:
            p[1] = quantity

def display_stock(stock):
    if not stock:
        print("Stock is empty")
    for p in stock:
        print(f"Name: {p[0]}, Quantity: {p[1]}, Price: {p[2]}")
