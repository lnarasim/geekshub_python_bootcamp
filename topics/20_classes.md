layout: true
class: center, middle, inverse

---

# OO Basics
with [examples](examples/20_classes.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Object Oriented
- It is a paradigm
- Solve problems by modeling objects and their relationships
- Building OO software involves knowing the following.
    - OO Analysis
    - OO Design
    - OO Programming

---

# What is OO?
- Solving problem by decomposing as objects.
- Object has certain properties/attributes
- Object has certain functionalities/behaviors
- Example: A human being has nose, ear, mouth and performs breath, hear and speak (or eat)
- Specific way to model a solution
- It is a programming paradigm

---

# Classes
- Classes are center of OOP
- Classes are blueprint or template of objects
- Object is born out of classes
- A class has a name
- A class defines an object
    - properties/attributes
    - methods

---

# Object
- Is a thing
- Has an identity
- Attributes (that defines the state of the object)
- Behavior (that changes the state of the object)
- Not restricted to Physical items such as Car, Wheels or visible items like Apple, Eye, Body
- Any concepts can be an object
- Usually a noun is an object, the thing that you can add "The" before it like "The Event", "The Bank Account", "The Match", "The Score" and so on

---

# Abstraction
- Focus on essential qualities
- Leaving unimportant and irrelevant details
- A customer object of restaurant application need not generally worry on the kind of car she has
- A mechanic who changes the tyre of a car need not worry on how air-conditioning in car works

---

# Encapsulation
- Surround something
- Keeps the content intact
- Protect the content
- Restrict the access
    - Ex: Medicine capsule
    - Helps changing the implementation with breaking the interface
    - Encapsulation is not do with keeping your idea secret but to reduce dependencies amongst different parts of the software
    - Change in one part of the software does not cascade to others parts.
    - Ex: If I change the car's tyre should not force me to change the engine for the car to function.

---

# Inheritance
- Code Reuse
- Ex: Person, Employee, Father, Customer
- Super Class - Sub Class, Parent Class - Child Class

---

# Polymorphism
- Many forms
- "+" adds integers, concatenates string
- Overriding

---

# Relationships
- "is-a" relation
- "has-a" relation

---

class: center, middle, inverse

# Classes in Python

---

layout: false

# Classes in Python
* define a class using class Dog:
* Has a special function \_\_init\_\_ that initializes the object
* Has attributes
* Has methods
* Attributes can be added on the fly (no need to define prior)

---

# Instance Attributes
* Defines the state of the object
* Unique to each object
* When the state changes in one object, it does not affect other objects
* Specified/initialized in \_\_init\_\_ method
* Attributes can be added or deleted dynamically from objects

---

# Instance Methods
* Behavior of objects
* Changes the state of the object
* Python passes object reference while calling instance method
* All object methods should have reference to itself and it should be the first argument
* _self_ is the convention

---

# An Example
* Let us see an example
    ```python
        class BankAccount:
            number_of_accounts = 0
            
            def __init__(self, name, account_number, opening_balance):
                BankAccount.number_of_accounts += 1
                self.name = name
                self.account_number = account_number
                self.balance = opening_balance
            
            def display(self):
                print("Name = ", self.name)
                print("Account Number = ", self.account_number)
                print("Balance = ", self.balance)

        an_account = BankAccount("Lakshmi", "123456789", 10000)
        an_account.display()
        print("Number of accounts = ", BankAccount.number_of_accounts)
        ```

        Name =  Lakshmi
        Account Number =  123456789
        Balance =  10000
        Number of accounts =  1
---

# Class Attributes
- Data to be shared amongst all objects
- class.dict()

---

# Class Methods 
- @classmethod
- class is passed as first argument (like self in objects)
- can be accessed using class and objects
- class methods can be used to create objects (can be used as constructor)

---

# Static methods
- @staticmethod
- Packages or falls in the namespace of the class.
- Does not pass self or class
- just another method/function inside the class
- If a method does not use self or class, it is the candidate to be static method 

---

# Inheritance
- class Dog(Mammal):
- all class automatically inherits object
- help(Dog) for method resolution
- call super class initializer as super.\_\_init\_\_()
- call super class initializer as Mammal.\_\_init\_\_(self)
- isinstance
- issubclass

---

# Magic methods 
- double underscore methods 
- \_\_repr\_\_ (falls back if \_\_str\_\_ is not defined)
- \_\_str\_\_
- \_\_add\_\_
- \_\_len\_\_
- \_\_eq\_\_
- \_\_gt\_\_
- \_\_lt\_\_
- Refer Python datamodel for various other dunder methods

---

# Property Decorators
- Use \_\_private_variable (convention for class mangling)
- @property (getter)
- @propertyname.setter
- @propertyname.deleter

---

# Monkey Patching
- Methods are just another object
- Change the behavior of the method by changing the method
    ```python
    class BankAccount:
        def __init_(self):
            pass
        def display(self):
            print("I am bank account")

    def display(self):
        print("I am monkey")

    account = BankAccount()
    BankAccount.display = display
    account.display()
    ```

---

# Exercises

1. Create a class "BankAccount" with attributes - account number, name and balance. Add few methods such as deposit and withdraw.

2. Create two objects for BankAccount, for two customers

3. Create a class attribute "number of accounts" to track number of accounts created

4. Create a class method to display "number of accounts"

5. List all the attributes/methods in the class

6. List all the attributes/methods in an object

7. Add an attribute to a class (in runtime)

8. Add an attribute to one of the objects (after the object is created)

9. Get the attributes value from the object that is used in previous example

10. Try to get attributes value from different object

---

# Exercises (Cntd)

11. Access the class attribute using object reference

12. Access the class attribute using class reference

13. How attributes/methods get resolved for object?

14. How attributes/methods get resolved for a class?

15. How to delete an attribute from class or object?

16. What is the first argument of object methods?

17. What is the first argument of class methods?

18. Any class is subclass of "object" - Is True or False?

19. Implement \_\_del\_\_ and observe what happens

20. When \_\_del\_\_ is called?

---

# Exercises (Cntd)

21. For BankAccount class, implement the following
    * ==
    * !=
    * \>=
    * <=
    * \>
    * \<

22. Implement a stack using class with simple operations - push and pop

23. Implement a queue using class with simple operations - enqueue and dequeue

24. Implement a Linked List using class with simple operations of add, edit, delete and iterate the list

25. Implement a binary tree with insert and delete operations. Implement all traversals (inorder, preorder and postorder)

---

layout: true
class: center, middle, inverse

---

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)