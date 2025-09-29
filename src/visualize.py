# visualize.py
import matplotlib.pyplot as plt
from stock import stock

def bar_chart():
    if not stock:
        print("Stock is empty. No chart to display.")
        return
    names = [p[0] for p in stock]
    quantities = [p[1] for p in stock]
    plt.bar(names, quantities, color='skyblue')
    plt.xlabel("Products")
    plt.ylabel("Quantity")
    plt.title("Quantity per Product")
    plt.show()

def pie_chart():
    if not stock:
        print("Stock is empty. No chart to display.")
        return
    names = [p[0] for p in stock]
    values = [p[1] * p[2] for p in stock]
    plt.pie(values, labels=names, autopct='%1.1f%%', startangle=90)
    plt.title("Stock Value Distribution")
    plt.show()
