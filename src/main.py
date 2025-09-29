# main.py
from stock import add_product, remove_product, update_quantity, display_stock
from stats import total_value, price_mean, price_min, price_max, most_expensive, cheapest
from visualize import bar_chart, pie_chart
from menu import show_menu

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Product name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Unit price: "))
        add_product(name, quantity, price)
        print(f"{name} added successfully!\n")

    elif choice == "2":
        name = input("Product name to remove: ")
        remove_product(name)
        print(f"{name} removed successfully!\n")

    elif choice == "3":
        name = input("Product name to update: ")
        quantity = int(input("New quantity: "))
        update_quantity(name, quantity)
        print(f"{name} quantity updated!\n")

    elif choice == "4":
        print("\nCurrent Stock:")
        display_stock()
        print()

    elif choice == "5":
        print("\nStock Statistics:")
        print(f"Total value: {total_value()}")
        print(f"Average unit price: {price_mean():.2f}")
        print(f"Minimum unit price: {price_min():.2f}")
        print(f"Maximum unit price: {price_max():.2f}")
        expensive = most_expensive()
        cheap = cheapest()
        if expensive:
            print(f"Most expensive product: {expensive[0]} (Price: {expensive[2]}, Quantity: {expensive[1]})")
        if cheap:
            print(f"Cheapest product: {cheap[0]} (Price: {cheap[2]}, Quantity: {cheap[1]})")
        print()

    elif choice == "6":
        chart = input("Which chart? (bar/pie): ").lower()
        if chart == "bar":
            bar_chart()
        elif chart == "pie":
            pie_chart()
        else:
            print("Invalid chart type!\n")

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.\n")
