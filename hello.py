# Basic Student Information System

# Create an empty dictionary to store students
students = {}

def add_student(student_id, name, course):
    """Adds a new student to the system."""
    students[student_id] = {"name": name, "course": course}
    print(f"✅ Successfully added: {name}")

def view_students():
    """Displays all students in the system."""
    print("\n--- 🎓 Enrolled Students ---")
    if not students:
        print("No students enrolled yet.")
    else:
        for student_id, info in students.items():
            print(f"ID: {student_id} | Name: {info['name']} | Course: {info['course']}")
    print("----------------------------\n")

# --- Testing the System ---
add_student("2026-0001", "Justin M.", "BSIT")
add_student("2026-0002", "Banana Ketchup", "BSIT")

view_students()
