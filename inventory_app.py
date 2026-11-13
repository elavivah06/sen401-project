"""Inventory application — Lab 3."""

from inventory import inventory, total_stock_value
from utils.helpers import highest_stock_item, lowest_stock_item


def main():
    print("=" * 45)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45)
    for item in inventory:
        print(f"{item['item_name']:<12} qty={item['quantity']:<5} price=${item['price']:.2f}")

    print("-" * 45)
    print(f"Total stock value: ${total_stock_value(inventory):,.2f}")

    hi = highest_stock_item(inventory)
    lo = lowest_stock_item(inventory)
    print(f"Highest stock: {hi['item_name']} ({hi['quantity']})")
    print(f"Lowest stock:  {lo['item_name']} ({lo['quantity']})")


if __name__ == "__main__":
    main()