import matplotlib.pyplot as plt



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

names = [item[0] for item in stock]
quantities = [item[1] for item in stock]



noms = [produit[0] for produit in stock]
valeur=[produit[1] * produit[2] for produit in stock]

plt.pie(valeur, labels=names) 
plt.bar(names, quantities)

plt.show()
