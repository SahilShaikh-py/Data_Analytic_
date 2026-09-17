"""
=============================================================================
TOPIC 04: OOP 4 PILLARS (OBJECT-ORIENTED PROGRAMMING)
=============================================================================
Author: Python Mastery Course
Level: Beginner to Intermediate

Conceptual Overview (4 Pillars of OOP):
----------------------------------------
1. ENCAPSULATION (Data Hiding & Protection):
   - Bundling data (variables) and methods (functions) into a single unit (class)
     while restricting direct access to internal state.
   - Public: `self.name` (Accessible from anywhere).
   - Protected: `self._name` (Convention: Intended for internal class and subclass use).
   - Private: `self.__balance` (Restricted from direct external access; accessed via getters/setters).

2. ABSTRACTION (Hiding Implementation, Exposing Functionality):
   - Exposing only the essential interface to the user while concealing complex internal logic.
   - Analogy: Pressing a car's accelerator moves it forward; the internal combustion and
     fuel injection processes remain abstracted from the driver.
   - Implemented in Python using the `abc` module with `ABC` and `@abstractmethod`.

3. INHERITANCE (Code Reusability & Class Hierarchy):
   - Deriving a child (derived) class from a parent (base) class to inherit attributes and methods.
   - Types: Single, Multilevel, Multiple, Hierarchical.
   - `super()`: Invokes the parent class constructor and methods from within a subclass.

4. POLYMORPHISM (Many Forms / Unified Interface):
   - The ability of different classes to respond to the same method call in ways specific to their type.
   - Types: Method Overriding, Duck Typing, Operator Overloading (`__add__`, `__gt__`).
=============================================================================
"""

from abc import ABC, abstractmethod

# =============================================================================
# PILLAR 1: ENCAPSULATION (DATA HIDING & GETTER/SETTER)
# =============================================================================
print("=" * 65)
print(">>> PILLAR 1: ENCAPSULATION (Bank Account Example) <<<")
print("=" * 65)

class BankAccount:
    """Bank Account class demonstrating Public, Protected, and Private attributes."""
    
    def __init__(self, account_holder, initial_balance, pin):
        self.account_holder = account_holder  # Public Variable (Freely accessible)
        self._branch = "Main Branch, Mumbai"  # Protected Variable (For class and subclasses)
        self.__balance = initial_balance      # Private Variable (Restricted from direct external access)
        self.__pin = pin                      # Private Variable

    # Getter Method (@property): For controlled read access to balance
    @property
    def balance(self):
        """Secure getter method to read account balance."""
        return self.__balance

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"  [+] ₹{amount:,} deposited successfully. Current Balance: ₹{self.__balance:,}")
        else:
            print("  [!] Deposit amount must be greater than 0.")

    # Withdraw Method with PIN verification
    def withdraw(self, amount, entered_pin):
        if entered_pin != self.__pin:
            print("  [X] Authentication Failed: Incorrect PIN entered!")
            return False
        if amount > self.__balance:
            print("  [X] Insufficient Balance! Not enough funds in account.")
            return False
        
        self.__balance -= amount
        print(f"  [-] ₹{amount:,} withdrawn successfully. Remaining Balance: ₹{self.__balance:,}")
        return True


# Demonstrating Encapsulation
acc = BankAccount("Rohit Sharma", 50000, 1234)
print(f"• Account Holder (Public) : {acc.account_holder}")
print(f"• Branch (Protected)      : {acc._branch}")
print(f"• Balance via Getter      : ₹{acc.balance:,}")

# Attempting direct private variable access (Raises AttributeError)
try:
    print(acc.__balance)
except AttributeError:
    print("• Security Check: acc.__balance cannot be accessed directly! (Encapsulation verified)")

# Proper deposit and withdrawal
acc.deposit(15000)
acc.withdraw(20000, 9999)  # Incorrect PIN
acc.withdraw(20000, 1234)  # Correct PIN

# --- Additional Example: Encapsulation (Student Marks) ---
print("\n--- Additional Example: Encapsulation (Student Marks) ---")
class Student:
    """Class to demonstrate getting and setting private data safely."""
    def __init__(self, name, marks):
        self.name = name          # Public
        self.__marks = marks      # Private

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print(f"  [+] Marks updated successfully for {self.name}.")
        else:
            print("  [X] Invalid marks! Must be between 0 and 100.")

std = Student("Aman", 85)
print(f"• Student Name: {std.name}")
print(f"• Marks (via Getter): {std.get_marks()}")
std.set_marks(105)  # Validation check failure
std.set_marks(92)   # Valid update
print(f"• Updated Marks: {std.get_marks()}")


# =============================================================================
# PILLAR 2: ABSTRACTION (ABC & ABSTRACT METHODS)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PILLAR 2: ABSTRACTION (Payment Gateway Example) <<<")
print("=" * 65)

# Abstract Base Class (Blueprint for all Payment Processors)
class PaymentGateway(ABC):
    """
    Abstract Class: Direct instances of this class CANNOT be instantiated.
    It enforces that every concrete child class must implement 'process_payment' and 'refund_payment'.
    """
    
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, transaction_id):
        pass

    # Concrete Method (Shared logic across all subclasses)
    def generate_receipt(self, txn_id, amount):
        print(f"  [Receipt] Transaction ID #{txn_id} | Amount: ₹{amount:,} | Status: COMPLETED")


# Child Class 1: UPI Payment
class UPIPayment(PaymentGateway):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"  [UPI] ₹{amount:,} deducted from UPI ID: {self.upi_id}")
        self.generate_receipt("UPI-987654", amount)

    def refund_payment(self, transaction_id):
        print(f"  [UPI] Refund of Txn #{transaction_id} processed back to {self.upi_id}")


# Child Class 2: Credit Card Payment
class CreditCardPayment(PaymentGateway):
    def __init__(self, card_number):
        self.masked_card = f"XXXX-XXXX-XXXX-{card_number[-4:]}"

    def process_payment(self, amount):
        print(f"  [Card] ₹{amount:,} charged to Credit Card: {self.masked_card}")
        self.generate_receipt("CC-112233", amount)

    def refund_payment(self, transaction_id):
        print(f"  [Card] Refund of Txn #{transaction_id} initiated to {self.masked_card}")


print("\n--- Demonstrating Abstraction & Interfaces ---")
upi = UPIPayment("user@oksbi")
upi.process_payment(2500)

print()
card = CreditCardPayment("4111222233334444")
card.process_payment(12000)

# --- Additional Example: Abstraction (Shape Area) ---
print("\n--- Additional Example: Abstraction (Shape Area) ---")
class Shape(ABC):
    """Abstract base class for all geometric shapes."""
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

circle = Circle(5)
rect = Rectangle(4, 6)
print(f"• Circle Area: {circle.area()}")
print(f"• Rectangle Area: {rect.area()}")


# =============================================================================
# PILLAR 3: INHERITANCE (SINGLE, MULTILEVEL, MULTIPLE & SUPER())
# =============================================================================
print("\n" + "=" * 65)
print(">>> PILLAR 3: INHERITANCE (Hierarchy & Reusability) <<<")
print("=" * 65)

# 1. Base Class (Parent)
class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Base Salary: ₹{self.base_salary:,}"


# 2. Single Inheritance (Child extends Parent)
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_language):
        # super() invokes the parent class constructor
        super().__init__(emp_id, name, base_salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"  • {self.name} is writing code in {self.programming_language}.")


# 3. Multilevel Inheritance (Grandchild extends Child)
class SeniorDeveloper(Developer):
    def __init__(self, emp_id, name, base_salary, programming_language, team_size):
        super().__init__(emp_id, name, base_salary, programming_language)
        self.team_size = team_size

    def conduct_code_review(self):
        print(f"  • {self.name} is reviewing code for a team of {self.team_size} devs.")


# 4. Multiple Inheritance (Child inherits from 2 separate Parents)
class SecurityClearance:
    def verify_clearance(self):
        return "Top Secret Clearance Verified"

class CyberSecurityAnalyst(Employee, SecurityClearance):
    def __init__(self, emp_id, name, base_salary, tool):
        Employee.__init__(self, emp_id, name, base_salary)
        self.tool = tool

    def perform_security_audit(self):
        clearance = self.verify_clearance()
        print(f"  • {self.name} performing audit using {self.tool}. ({clearance})")


print("\n--- Demonstrating Inheritance Types ---")
dev = Developer(101, "Sameer Khan", 60000, "Python")
print(dev.get_details())
dev.write_code()

print("\n--- Senior Developer (Multilevel) ---")
sr_dev = SeniorDeveloper(102, "Kavita Rao", 120000, "Python & Rust", 8)
print(sr_dev.get_details())
sr_dev.conduct_code_review()

print("\n--- Cyber Analyst (Multiple Inheritance) ---")
analyst = CyberSecurityAnalyst(103, "Rajiv Nair", 85000, "Wireshark & Splunk")
print(analyst.get_details())
analyst.perform_security_audit()

# --- Additional Example: Inheritance (Vehicle System) ---
print("\n--- Additional Example: Inheritance (Vehicle System) ---")
class Vehicle:
    """Base class for all vehicles."""
    def __init__(self, brand):
        self.brand = brand
    def start_engine(self):
        return f"{self.brand} engine started."

class Car(Vehicle):
    """Child class inheriting from Vehicle."""
    def drive(self):
        return f"{self.brand} car is driving."

class Bike(Vehicle):
    """Child class inheriting from Vehicle."""
    def ride(self):
        return f"{self.brand} bike is riding."

my_car = Car("Toyota")
my_bike = Bike("Honda")
print(f"• {my_car.start_engine()} -> {my_car.drive()}")
print(f"• {my_bike.start_engine()} -> {my_bike.ride()}")


# =============================================================================
# PILLAR 4: POLYMORPHISM (OVERRIDING & OPERATOR OVERLOADING)
# =============================================================================
print("\n" + "=" * 65)
print(">>> PILLAR 4: POLYMORPHISM (Many Forms) <<<")
print("=" * 65)

# 1. Method Overriding (Different Classes implementing the same method signature)
class Animal:
    def make_sound(self):
        return "Generic Animal Sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

print("\n--- 1. Polymorphism via Method Overriding ---")
animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(f"• {a.__class__.__name__} sound: {a.make_sound()}")


# 2. Operator Overloading (Customizing '+' and '>' for Objects)
class ShoppingCart:
    def __init__(self, user_name, total_bill):
        self.user_name = user_name
        self.total_bill = total_bill

    # __add__ operator overloading (+)
    def __add__(self, other):
        combined_bill = self.total_bill + other.total_bill
        return ShoppingCart(f"{self.user_name} & {other.user_name}", combined_bill)

    # __gt__ operator overloading (>)
    def __gt__(self, other):
        return self.total_bill > other.total_bill

    def __str__(self):
        return f"Cart of [{self.user_name}]: Total = ₹{self.total_bill:,}"


print("\n--- 2. Polymorphism via Operator Overloading ---")
cart1 = ShoppingCart("Arman", 4500)
cart2 = ShoppingCart("Suresh", 6200)

print(f"• Cart 1: {cart1}")
print(f"• Cart 2: {cart2}")

# The '+' operator combines two shopping carts (__add__ dunder method)
combo_cart = cart1 + cart2
print(f"• Combined Cart (+ operator): {combo_cart}")

# The '>' operator compares cart totals (__gt__ dunder method)
is_cart2_bigger = cart2 > cart1
print(f"• Is Cart 2 bill greater than Cart 1? : {is_cart2_bigger}")

# --- Additional Example: Polymorphism (Duck Typing) ---
print("\n--- Additional Example: Polymorphism (Duck Typing) ---")
class Bird:
    def fly(self):
        print("  • Bird is flying in the sky.")

class Airplane:
    def fly(self):
        print("  • Airplane is flying using engines.")

def let_it_fly(flying_object):
    # This function works on any object providing a 'fly' method (Duck Typing)
    flying_object.fly()

sparrow = Bird()
boeing = Airplane()
let_it_fly(sparrow)
let_it_fly(boeing)

print("\n" + "=" * 65)
print(">>> TOPIC 04 (4 PILLARS OF OOP) COMPLETED SUCCESSFULLY! <<<")
print("=" * 65)
