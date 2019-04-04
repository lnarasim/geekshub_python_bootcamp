name: inverse
layout: true
class: center, middle, inverse

---

# Classes in Python
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Classes in Python
* define a class using class Dog:
* Has a special function \_\_init\_\_ that initializes the object
* Has attributes
* Has methods
* Attributes can be added on the fly (no need to define prior)

---

# Class variables
- Data should be shared amongst all objects
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