import numpy as np


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


def total_value(stock):
    total_value= sum([item[1] * item[2] for item in stock])
    return total_value
print(total_value(stock))


def average_price():
    average= np.mean([item[2] for item in stock])
    return average

print(average_price())


def price_min():
    min_price= min([item[2] for item in stock])
    return min_price
print(price_min())

def price_max():
    max_price= max([item[2] for item in stock])
    return max_price
print(price_max())


def expensive_product():
    expensive= max(stock, key=lambda item: item[2])
    return expensive    
print(expensive_product())


def cheapest_product():
    expensive= min(stock, key=lambda item: item[2])
    return expensive    
print(cheapest_product())