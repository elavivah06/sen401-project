"""SQLite database layer — Lab 4 migration."""
import sqlite3

DB_PATH = "student_app.db"


def get_connection():
    """Open a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create tables if they don't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score REAL NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        """)
        conn.commit()


def insert_student(name: str, score: float):
    with get_connection() as conn:
        conn.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
        conn.commit()


def fetch_students() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("SELECT name, score FROM students").fetchall()
    return [{"name": r[0], "score": r[1]} for r in rows]


def insert_inventory_item(item_name: str, quantity: int, price: float):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)",
            (item_name, quantity, price),
        )
        conn.commit()


def fetch_inventory() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("SELECT item_name, quantity, price FROM inventory").fetchall()
    return [{"item_name": r[0], "quantity": r[1], "price": r[2]} for r in rows]