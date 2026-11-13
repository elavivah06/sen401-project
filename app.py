"""Main app — Lab 4 refactored entry point."""
from database import init_db
from controllers import add_student, add_inventory_item, get_student_stats, get_inventory_stats


def main():
    init_db()
    print("=" * 50)
    print("REFACTORED APP (SQLite-backed)")
    print("=" * 50)

    # Seed demo data
    add_student("James", 45)
    add_student("Deborah", 82)
    add_student("Aisha", 67)

    add_inventory_item("Laptop", 10, 1500.0)
    add_inventory_item("Mouse", 50, 20.0)

    print("\nStudent Stats:", get_student_stats())
    print("Inventory Stats:", get_inventory_stats())


if __name__ == "__main__":
    main()