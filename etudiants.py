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

    def rank_matter_1(self):
        print("\n--- Classement en Matière 1 (ordre décroissant) ---")
        sorted_students = sorted(self.students, key=lambda s: s.grades[0], reverse=True)
        for s in sorted_students:
            print(f"  {s.name}: {s.grades[0]}")

    def rank_matter_2(self):
        print("\n--- Classement en Matière 2 (ordre décroissant) ---")
        sorted_students = sorted(self.students, key=lambda s: s.grades[1], reverse=True)
        for s in sorted_students:
            print(f"  {s.name}: {s.grades[1]}")

    def rank_matter_3(self):
        print("\n--- Classement en Matière 3 (ordre décroissant) ---")
        sorted_students = sorted(self.students, key=lambda s: s.grades[2], reverse=True)
        for s in sorted_students:
            print(f"  {s.name}: {s.grades[2]}")

school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

school_class.display_by_subject()
school_class.display_averages()
school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()

