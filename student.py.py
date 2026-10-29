students = []

def add_student(name, roll_no):
    students.append({"Name": name, "Roll No": roll_no})

def display_students():
    for student in students:
        print(student)

add_student("Shreshth", 18)
add_student("Somya", 21)

display_students()