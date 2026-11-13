"""Main demo application for the Student Management System."""

from students import students, average_score, add_student
from utils.helpers import highest_score, lowest_score


def main():
    """Run the demo app."""
    print("Current Students:", students)
    print("Average Score:", average_score(students))

    top = highest_score(students)
    bottom = lowest_score(students)
    print(f"Highest Score: {top['name']} - {top['score']}")
    print(f"Lowest Score: {bottom['name']} - {bottom['score']}")

    add_student("New Student", 70)
    print("After adding a student:")
    print("Current Students:", students)


if __name__ == "__main__":
    main()