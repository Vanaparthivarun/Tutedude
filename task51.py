student_marks = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 92
}
student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")