"""Business logic controllers — Lab 4 refactor."""
from models import Student, InventoryItem
from database import (
    insert_student, fetch_students,
    insert_inventory_item, fetch_inventory,
)
from utils.helpers import highest_score, lowest_score, highest_stock_item, lowest_stock_item


def add_student(name: str, score: float) -> Student:
    """Validate and persist a new student."""
    student = Student(name=name, score=score)
    insert_student(student.name, student.score)
    return student


def add_inventory_item(item_name: str, quantity: int, price: float) -> InventoryItem:
    """Validate and persist a new inventory item."""
    item = InventoryItem(item_name=item_name, quantity=quantity, price=price)
    insert_inventory_item(item.item_name, item.quantity, item.price)
    return item


def get_student_stats() -> dict:
    data = fetch_students()
    if not data:
        return {"count": 0, "average": 0, "highest": None, "lowest": None}
    return {
        "count": len(data),
        "average": sum(s["score"] for s in data) / len(data),
        "highest": highest_score(data),
        "lowest": lowest_score(data),
    }


def get_inventory_stats() -> dict:
    data = fetch_inventory()
    total = sum(i["quantity"] * i["price"] for i in data)
    return {
        "count": len(data),
        "total_value": total,
        "highest": highest_stock_item(data),
        "lowest": lowest_stock_item(data),
    }