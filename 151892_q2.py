class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for assignment, grade in self.assignments.items():
            print(f"  {assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to the course.")

    def assign_grade(self, student, assignment_name, grade):
        student.add_assignment(assignment_name, grade)

    def display_students(self):
        print(f"Students in course '{self.course_name}':")
        for student in self.students:
            print(f"  {student.name} (ID: {student.student_id})")
            student.display_grades()

    def interactive_mode(self):
        while True:
            print("\nOptions:")
            print("1: Add a student")
            print("2: Assign a grade to a student")
            print("3: Display all students and their grades")
            print("4: Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                student = Student(name, student_id)
                self.add_student(student)
            
            elif choice == "2":
                student_id = input("Enter student ID: ")
                assignment_name = input("Enter assignment name: ")
                grade = input("Enter grade: ")
                student = next((s for s in self.students if s.student_id == student_id), None)
                if student:
                    self.assign_grade(student, assignment_name, grade)
                else:
                    print("Student not found.")
            
            elif choice == "3":
                self.display_students()
            
            elif choice == "4":
                print("Exiting interactive mode.")
                break
            
            else:
                print("Invalid choice. Please try again.")

