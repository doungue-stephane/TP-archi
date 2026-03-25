from collections.abc import Iterable, Iterator

def add_fourth_matter(cls):
    original_init = cls.__init__

    def new_init(self, name, grade1, grade2, grade3, grade4=0):
        original_init(self, name, grade1, grade2, grade3)
        self.grades.append(grade4)

    cls.__init__ = new_init
    return cls


@add_fourth_matter
class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grades = [grade1, grade2, grade3]

    def average(self):
        return sum(self.grades) / len(self.grades)


class StudentIterator(Iterator):
    def __init__(self, students, matter_index=0):
        # Trier du meilleur au plus mauvais selon la matière spécifiée
        self._students = sorted(students, key=lambda s: s.grades[matter_index], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

class StudentIteratorMatter1(StudentIterator):
    def __init__(self, students):
        super().__init__(students, matter_index=0)


class StudentIteratorMatter2(StudentIterator):
    def __init__(self, students):
        super().__init__(students, matter_index=1)


class StudentIteratorMatter3(StudentIterator):
    def __init__(self, students):
        super().__init__(students, matter_index=2)

class StudentIteratorMatter4(StudentIterator):
    def __init__(self, students):
        super().__init__(students, matter_index=3)

def add_fourth_iterator(cls):
    def iter_matter_4(self):
        return StudentIteratorMatter4(self.students)
    cls.iter_matter_4 = iter_matter_4
    return cls


@add_fourth_iterator
class SchoolClass:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'students'):  # Pour éviter la réinitialisation
            self.students = []
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __iter__(self):
        return StudentIterator(self.students)
    
    def iter_matter_2(self):
        return StudentIteratorMatter2(self.students)

    def iter_matter_3(self):
        return StudentIteratorMatter3(self.students)

    def add_student(self, student):
        self.students.append(student)

    def display_by_subject(self):
        subjects = ["Matière 1", "Matière 2", "Matière 3", "Matière 4"]
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
    
    def rank_matter_4(self):
        print("\n--- Classement en Matière 4 (ordre décroissant) ---")
        sorted_students = sorted(self.students, key=lambda s: s.grades[3], reverse=True)
        for s in sorted_students:
            print(f"  {s.name}: {s.grades[3]}")


school_class = SchoolClass.get_instance()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

school_class.display_by_subject()
school_class.display_averages()
school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()
school_class.rank_matter_4()


print("\n--- Itération via __iter__ (classement Matière 1) ---")
for student in school_class:
    print(f"  {student.name}: {student.grades[0]}")

print("\n--- Itération Matière 2 ---")
for student in school_class.iter_matter_2():
    print(f"  {student.name}: {student.grades[1]}")

print("\n--- Itération Matière 3 ---")
for student in school_class.iter_matter_3():
    print(f"  {student.name}: {student.grades[2]}")

print("\n--- Itération Matière 4 ---")
for student in school_class.iter_matter_4():
    print(f"  {student.name}: {student.grades[3]}")

# Démonstration du singleton
another_instance = SchoolClass.get_instance()
print(f"\nInstance unique : {school_class is another_instance}")