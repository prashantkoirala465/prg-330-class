# Week 3 Grade Calculator

import grade
import result

student = 1

while student <= 3:

    print("\nStudent", student)

    name = input("Enter student name: ")
    score = float(input("Enter exam score: "))

    print("Student Name:", name)
    print("Exam Score:", score)

    grade.show_grade(score)
    result.show_result(score)

    student = student + 1
