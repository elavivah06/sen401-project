# Reverse Engineering Notes (Lab 4)

## Module Dependencies
- `app.py` imports from `students.py` and `utils.helpers`
- `inventory_app.py` imports from `inventory.py` and `utils.helpers`
- Both apps share `utils.helpers` (common utility layer)

## Code Smells Identified
1. **High coupling:** `app.py` directly manipulates global `students` list.
2. **Data in memory only:** No persistent storage → data lost on restart.
3. **Duplicated logic:** Score/quantity aggregations duplicated.

## Refactoring Plan
1. Introduce **models.py** for Pydantic schemas.
2. Introduce **controllers.py** for business logic.
3. Introduce **database.py** for SQLite persistence.
4. Migrate JSON data → SQLite.
5. Containerize with Docker Compose.