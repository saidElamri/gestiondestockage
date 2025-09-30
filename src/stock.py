stock = [ ["Laptop", 15, 1200.50],
    ["Mouse", 50, 25.99],
    ["Keyboard", 30, 45.00],
    ["Monitor", 20, 220.75],
    ["USB Cable", 100, 5.50],
    ["Headphones", 25, 75.20],
    ["Webcam", 10, 60.00],
    ["External HDD", 12, 110.00],
    ["Smartphone", 18, 800.99],
    ["Charger", 40, 18.75]]  # each product = ["name", quantity, unit_price]


def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    unit_price = float(input("Enter product unit price: "))
    new_product = [name, quantity, unit_price]
    stock.append(new_product)
    print(f"Product {name} added successfully.")
    return stock

print(add_product())


def delete_product():
    name=input("Enter product name to delete: ")
    if name in stock:
        stock.remove(name)
    print(f"Product {name} deleted successfully.")
    return stock
print(delete_product())



def update_stock():
    name= input("Enter product name to update: ")
    for product in stock:
        if product [0] == name:
            quantity = int(input("Enter new quantity: "))
            unit_price = float(input("Enter new unit price: "))
            product[1] = quantity
            product[2] = unit_price
            print(f"Product {name} updated successfully.")
            return stock
        else:
            print(f"Product {name} not found.")
            return stock
        
print(update_stock())



def display_stock():
    for product in stock:
        print(f"Product: {product[0]}, Quantity: {product[1]}, Unit Price: ${product[2]}")
    return stock

print(display_stock())
        

