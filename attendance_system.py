# Attendance Management System

attendance = {}

while True:
    print("\n===== Attendance Management System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        student = input("Enter student name: ")
        attendance[student] = "Absent"
        print(student, "added successfully.")

    # Mark Attendance
    elif choice == '2':
        student = input("Enter student name: ")

        if student in attendance:
            status = input("Enter Present or Absent: ")
            attendance[student] = status
            print("Attendance updated.")
        else:
            print("Student not found.")

    # View Attendance
    elif choice == '3':
        print("\nAttendance Records:")

        for student, status in attendance.items():
            print(student, ":", status)

    # Exit
    elif choice == '4':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")