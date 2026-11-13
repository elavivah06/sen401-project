"""Inventory data module — Lab 3."""

inventory = [
    {"item_name": "Laptop", "quantity": 10, "price": 1500.00},
    {"item_name": "Mouse", "quantity": 50, "price": 20.00},
    {"item_name": "Keyboard", "quantity": 30, "price": 45.50},
    {"item_name": "Monitor", "quantity": 15, "price": 300.00},
]


def total_stock_value(data: list[dict]) -> float:
    """Corrective: handle empty list & sum quantity*price correctly."""
    if not data:
        return 0.0
    return sum(item["quantity"] * item["price"] for item in data)