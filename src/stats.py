# stats.py
import numpy as np
from stock import stock

def total_value(stock):
    """Return total value of the stock (sum of quantity * unit price)."""
    if not stock:
        return 0
    values = np.array([p[1] * p[2] for p in stock])
    return np.sum(values)

def price_mean(stock):
    """Return the mean unit price of products."""
    if not stock:
        return 0
    prices = np.array([p[2] for p in stock])
    return np.mean(prices)

def price_min(stock):
    """Return the minimum unit price."""
    if not stock:
        return 0
    prices = np.array([p[2] for p in stock])
    return np.min(prices)

def price_max(stock):
    """Return the maximum unit price."""
    if not stock:
        return 0
    prices = np.array([p[2] for p in stock])
    return np.max(prices)

def most_expensive(stock):
    """Return the product with the highest unit price."""
    if not stock:
        return None
    return max(stock, key=lambda x: x[2])

def cheapest(stock):
    """Return the product with the lowest unit price."""
    if not stock:
        return None
    return min(stock, key=lambda x: x[2])


