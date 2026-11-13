"""Student data module for the Student Management System."""

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Aisha", "score": 67},
    {"name": "Chinedu", "score": 91},
]


def average_score(data):
    """Return the average score of a list of student dicts."""
    if len(data) == 0:
        return 0  # Preventive maintenance: avoid division by zero
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    """Append a new student to the global list."""
    students.append({"name": name, "score": score})