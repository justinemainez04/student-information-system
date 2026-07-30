# Improved Student Information System

# Global dictionary to store students
students = {}

def add_student(student_id, name, course):
    """Adds a new student, checking for duplicates first."""
    if student_id in students:
        print(f"⚠️ Error: A student with ID '{student_id}' already exists!")
        return
    
    students[student_id] = {"name": name.strip(), "course": course.strip().upper()}
    print(f"✅ Successfully added: {name}")

def view_students():
    """Displays all students in a clean format."""
    print("\n--- 🎓 Enrolled Students ---")
    if not students:
        print("No students enrolled yet. Please add a student first.")
    else:
        for student_id, info in students.items():
            print(f"ID: {student_id} | Name: {info['name']} | Course: {info['course']}")
    print("----------------------------")

def main():
    """Main application loop."""
    print("Welcome to the Student Information System!")
    
    while True:
        print("\n📌 MAIN MENU")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n-- Add Student --")
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            course = input("Enter Course (e.g., BSIT): ").strip()
            
            # Basic validation to ensure no fields are left blank
            if student_id and name and course:
                add_student(student_id, name, course)
            else:
                print("⚠️ Error: All fields are required! Please try again.")
                
        elif choice == '2':
            view_students()
            
        elif choice == '3':
            print("👋 Exiting system. Goodbye!")
            break # Breaks out of the while loop to end the program
            
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

# This ensures the menu only runs if this file is executed directly
if __name__ == "__main__":
    main()
