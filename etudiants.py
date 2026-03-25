class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grades = [grade1, grade2, grade3]

    def average(self):
        return sum(self.grades) / len(self.grades)


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_by_subject(self):
        subjects = ["Matière 1", "Matière 2", "Matière 3"]
        for i, subject in enumerate(subjects):
            print(f"\n--- Classement en {subject} ---")
            sorted_students = sorted(self.students, key=lambda s: s.grades[i], reverse=True)
            for s in sorted_students:
                print(f"  {s.name}: {s.grades[i]}")

    def display_averages(self):
        print("\n--- Moyennes générales ---")
        sorted_students = sorted(self.students, key=lambda s: s.average(), reverse=True)
        for s in sorted_students:
            print(f"  {s.name}: {s.average():.2f}")

