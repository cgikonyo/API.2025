class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        if not self.assignments:
            print(f"{self.name} has no grades yet.")
        else:
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added {student.name} to {self.course_name}.")

    def assign_grade(self, student, assignment_name, grade):
        student.add_assignment(assignment_name, grade)
        print(f"Assigned {grade} to {student.name} for {assignment_name}.")

    def display_all_grades(self):
        for student in self.students:
            print(f"\nGrades for {student.name}:")
            student.display_grades()


# Interactive session
instructor = Instructor("Mr. Smith", "Python Programming")

while True:
    print("\n--- Course Management Menu ---")
    print("1. Add student")
    print("2. Assign grade")
    print("3. Display all grades")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        sid = input("Enter student ID: ")
        student = Student(name, sid)
        instructor.add_student(student)

    elif choice == "2":
        student_name = input("Enter student name: ")
        found_student = None
        for s in instructor.students:
            if s.name == student_name:
                found_student = s
                break
        if found_student:
            assignment = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(found_student, assignment, grade)
        else:
            print("Student not found.")

    elif choice == "3":
        instructor.display_all_grades()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")