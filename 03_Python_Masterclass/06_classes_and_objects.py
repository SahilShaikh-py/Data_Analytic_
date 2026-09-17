"""
=============================================================================
TOPIC 03: CLASSES, OBJECTS & METHODS IN PYTHON
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview:
--------------------
1. What is a Class?
   - A class is a Blueprint or Template defining properties (Variables/Data)
     and behaviors (Methods/Functions).
   - Real-world analogy: "Car" is a class (Design template).

2. What is an Object?
   - An object is a concrete instance of a class.
   - Real-world analogy: "Swift", "Scorpio", "BMW" are individual objects of the Car class.

3. The `__init__()` (Constructor) and `self` Keyword:
   - `__init__()`: A special constructor method called automatically when a new
     object is instantiated. Its purpose is to initialize instance attributes.
   - `self`: Refers to the current instance of the class. It allows each object
     to access and modify its own attributes and methods independently.

4. Types of Variables:
   - Instance Variables: Unique to each object (e.g., student roll number, name).
   - Class Variables: Shared across all instances of the class (e.g., institute name).

5. Three Types of Methods:
   - Instance Method: Takes `self` as the first parameter; accesses/modifies instance state.
   - Class Method: Decorated with `@classmethod` and takes `cls`; modifies class-level state.
   - Static Method: Decorated with `@staticmethod`; neither takes `self` nor `cls`. Acts as an independent utility function.
=============================================================================
"""

print("=" * 65)
print(">>> PART 1: CLASS, OBJECT & CONSTRUCTOR (__init__) <<<")
print("=" * 65)

class Student:
    # -------------------------------------------------------------
    # 1. Class Variable (Shared among all students)
    # -------------------------------------------------------------
    institute_name = "YSM Info Solution"
    total_students = 0

    # -------------------------------------------------------------
    # 2. Constructor (__init__ method)
    # -------------------------------------------------------------
    def __init__(self, roll_no, name, course, fees_paid):
        # Instance Variables (Unique data for each student)
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.fees_paid = fees_paid
        
        # Increment class-level student counter
        Student.total_students += 1

    # -------------------------------------------------------------
    # 3. Instance Method (Operates on individual student data)
    # -------------------------------------------------------------
    def display_details(self):
        """Displays basic details of the student."""
        print(f"  • Roll No : {self.roll_no}")
        print(f"  • Name    : {self.name}")
        print(f"  • Course  : {self.course}")
        print(f"  • Fees    : ₹{self.fees_paid:,}")
        print(f"  • Institute: {Student.institute_name}")

    def pay_additional_fees(self, amount):
        """Updates paid tuition fees for the student."""
        self.fees_paid += amount
        print(f"  [Update] {self.name} paid an additional ₹{amount:,}. Total Fees: ₹{self.fees_paid:,}")

    # -------------------------------------------------------------
    # 4. Class Method (@classmethod)
    # -------------------------------------------------------------
    @classmethod
    def change_institute_name(cls, new_name):
        """Updates the institute name across all instances."""
        cls.institute_name = new_name
        print(f"\n[Notice] Institute name changed to '{cls.institute_name}'.")

    @classmethod
    def get_total_students_count(cls):
        """Returns the total number of enrolled students."""
        return cls.total_students

    # -------------------------------------------------------------
    # 5. Static Method (@staticmethod)
    # -------------------------------------------------------------
    @staticmethod
    def is_passing_grade(marks):
        """General utility function that checks whether a score meets the passing threshold."""
        return marks >= 40

    # -------------------------------------------------------------
    # 6. Magic / Dunder Methods (__str__ and __repr__)
    # -------------------------------------------------------------
    def __str__(self):
        """User-friendly string representation when using print(obj)."""
        return f"Student(Roll: {self.roll_no}, Name: '{self.name}', Course: '{self.course}')"

    def __repr__(self):
        """Developer debugging representation."""
        return f"Student({self.roll_no}, '{self.name}', '{self.course}', {self.fees_paid})"


# -------------------------------------------------------------
# OBJECT CREATION & DEMONSTRATION
# -------------------------------------------------------------
print("\n--- Creating Student Objects ---")
student1 = Student(101, "Aman Verma", "Data Analytics", 25000)
student2 = Student(102, "Neha Sharma", "Cyber Security", 30000)
student3 = Student(103, "Rohan Gupta", "Full Stack Python", 28000)

print("\n--- Displaying Student Details (Instance Method) ---")
print("Student 1 Details:")
student1.display_details()

print("\nStudent 2 Details:")
student2.display_details()

# Instance method call to update fees
print("\n--- Updating Fees ---")
student1.pay_additional_fees(5000)

print("\n" + "=" * 65)
print(">>> PART 2: CLASS METHODS & STATIC METHODS <<<")
print("=" * 65)

# Total Students Count using Class Method
print(f"• Total Students Enrolled: {Student.get_total_students_count()}")

# Changing Institute Name using Class Method
Student.change_institute_name("YSM Institute of Advanced Tech")

# Check if institute name changed for all objects
print("\nChecking institute name after change:")
print(f"• Student 1 Institute: {student1.institute_name}")
print(f"• Student 2 Institute: {student2.institute_name}")

# Static Method Demo (Can be called directly on the class without an instance)
print("\n--- Static Method Demonstration ---")
marks_list = [78, 35, 92, 28]
for m in marks_list:
    status = "PASS" if Student.is_passing_grade(m) else "FAIL"
    print(f"• Marks: {m:>2} -> Result: {status}")

print("\n" + "=" * 65)
print(">>> PART 3: DUNDER / MAGIC METHODS (__str__ & __repr__) <<<")
print("=" * 65)

# When an object is passed to print(), __str__() is invoked automatically
print(f"• print(student1) : {student1}")
print(f"• repr(student2)  : {repr(student2)}")

print("\n" + "=" * 65)
print(">>> TOPIC 03 COMPLETED SUCCESSFULLY! <<<")
print("=" * 65)
