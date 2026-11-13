"""Main demo application for the Student Management System."""

from students import students, average_score, add_student, median_score
from utils.helpers import highest_score, lowest_score


def main():
    """Run the demo app."""
    print("=" * 40)
    print("STUDENT MANAGEMENT SYSTEM v1.1")
    print("=" * 40)
    print(f"Total students: {len(students)}")
    print(f"Average Score: {average_score(students):.2f}")
    print(f"Median Score:  {median_score(students):.2f}")

    top = highest_score(students)
    bottom = lowest_score(students)
    print(f"Highest Score: {top['name']} - {top['score']}")
    print(f"Lowest Score:  {bottom['name']} - {bottom['score']}")

    print("\n-- Adding valid student --")
    add_student("Grace", 88)

    print("\n-- Adding invalid students (should be rejected) --")
    add_student("Bad Score", 150)
    add_student("", 50)

    print(f"\nTotal students after update: {len(students)}")
    print(f"New Average: {average_score(students):.2f}")
    print(f"New Median:  {median_score(students):.2f}")


if __name__ == "__main__":
    main()