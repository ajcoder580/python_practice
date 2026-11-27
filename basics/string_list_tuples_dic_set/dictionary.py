n= int(input("Enter the size of your dictionary"))

s_data={}
for student in range(n):
    name=input("Enter the names of student")
    marks=int(input("Enter the marks of student"))
    s_data[name]=marks

print(s_data)


while True:
    print('''Operation you can perform on dictionary
        1.Enter "A" to add student
        2.Enter "B to Update marks
        3. Enter "C" to Search for student
        4.Enter "D" to Display all students and marks
        5.Enter "E" to Exit from program''')
    choice=input("Enter your choice(1-5)")

    if (choice=="1"):
        name = input("Enter student name: ")
        if name in s_data:
            print("Student already exists. Use option 2 to update marks.")
        else:
            marks = int(input("Enter marks: "))
            s_data[name] = marks
            print("Student added.")
    elif choice=="2":
        name = input("Enter student name: ")
        if name in s_data:
            marks=int(input("Enter new marks"))
            s_data.update({name:marks})
            print("Marks Updated")
        else:
            print("student not found")
    elif choice=="3":
        name = input("Enter student name to search: ")
        if name in s_data:
            print(name, "has scored", s_data[marks])
        else:
            print("Student not found")
    elif choice == '4':
        if len(s_data) == 0:
            print("No records available.")
        else:
            print("\nName\t\tMarks")
            for name, marks in s_data.items():
                print(name, "\t\t", marks)
    elif choice=='5':
        print("Goodby!")
        break
    else:
        print("Invalid choice. Try again.")


# info={
#     "Name":"Rahul",
#     "Stream":"MCA",
#     "Location":"Bihar",
#     "Session":2026-27
# }

# print(type(info))
# print(info)
# info.update({"hello":"bhai"})