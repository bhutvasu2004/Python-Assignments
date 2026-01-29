students={
    'Vasu': 85,
    'Amit': 92,
    'Riya': 78,
    'Sneha': 88,
    'Karan': 95
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")