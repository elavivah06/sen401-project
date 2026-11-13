"""Student data module for the Student Management System.

Maintenance updates:
- Corrective: validate score range (0-100) and name is non-empty.
- Adaptive: uses Python 3.12 features (type hints, f-strings).
- Perfective: added median_score() and cleaner output.
- Preventive: modular helper functions + docstrings.
"""

from statistics import median

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Aisha", "score": 67},
    {"name": "Chinedu", "score": 91},
]


def _is_valid_score(score):
    """Return True if score is a number between 0 and 100."""
    return isinstance(score, (int, float)) and 0 <= score <= 100


def average_score(data):
    """Return the average score of a list of student dicts."""
    if not data:
        return 0
    valid_scores = [d["score"] for d in data if _is_valid_score(d.get("score"))]
    if not valid_scores:
        return 0
    return sum(valid_scores) / len(valid_scores)


def median_score(data):
    """Return the median score (new in v1.1)."""
    if not data:
        return 0
    scores = [d["score"] for d in data if _is_valid_score(d.get("score"))]
    if not scores:
        return 0
    return median(scores)


def add_student(name, score):
    """Add a student after validating name and score.

    Corrective maintenance: reject invalid input instead of silently
    corrupting the data.
    """
    if not isinstance(name, str) or not name.strip():
        print(f"Invalid student data: name must be a non-empty string (got {name!r})")
        return
    if not _is_valid_score(score):
        print(f"Invalid student data: score must be between 0 and 100 (got {score!r})")
        return
    students.append({"name": name.strip(), "score": score})
    print(f"Added student: {name.strip()} ({score})")