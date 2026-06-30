from student import Student

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ")
        age = int(input("Enter Age : "))
        marks = float(input("Enter Marks : "))

        student = Student(student_id, name, age, marks)
        self.students.append(student)

        print("Student Added Successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No Students Found!")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        student_id = int(input("Enter Student ID to Search : "))

        for student in self.students:
            if student.student_id == student_id:
                print("Student Found!")
                student.display()
                return

        print("Student Not Found!")

    def update_marks(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("Enter New Marks : "))
                student.marks = new_marks
                print("Marks Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_topper(self):
        if len(self.students) == 0:
            print("No Students Available!")
        else:
            topper = self.students[0]

            for student in self.students:
                if student.marks > topper.marks:
                    topper = student

            print("\nTopper Details")
            topper.display()

