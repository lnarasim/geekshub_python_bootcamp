name: inverse
layout: true
class: center, middle, inverse

---

# Variables, Memory and Objects
with [examples](variables_memory_objects.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false


# References
- Assigning an object to a variable and making it to point to the object
- It is actual link or connection made
- One or more variables can point to an object

# Examples:
* number = 100 - number points to an object of the class "int"
* car = Car() - car points to an object of the class "Car"
* In this case
    * name is variable
    * 100 is an object
    * name pointing to 100 is reference
---

# Memory References
- An object can have one or more references
- Objects are created in heap
- Managed by Python Memory Manager
- Depending upon the scope, only references are stored in stack for local variables
- The objects live as long as there is at least one active/live reference pointing/referring to it
- When the number of references pointing to an object reaches zero, PVM's Garbage collector deletes and frees the object

---
# Reference Counting
- An object is created in heap
- When it is assigned to a variable, the reference count is increased
- Number of references of an object can be inspected by two ways
	- sys.getrefcout(variable_name)
    - ctypes.c_long.from_address(id(variable.name)).value
- Accesing using ctypes will give random results if the object is garbage collected
- Circular references

---

# Garbage Collection
 - Python remembers the reference count
 - When reference count reaches "zero", the object is deleted and GC reclaims the memory
 - Python handles circular references
 - Can be controlled using "gc" module
 - GC can be turned off (but do not do it) - gc.enable(), gc.disable()
 - Runs periodically
 - You can run GC (gc.collect())
 - gc.get_objects(), returns a list of objects managed by gc

---

# Dynamic Typing
* The type of object is stored along with object
* A variable can point to different types of object at different type
* A variable name is just an alias to the object
* Static typing: The type is stored along with variable, so they cannot point to object of different type
* Example:
    ```python
    var = 10
    var = "Hello"
    var = Car()
    ```

---

# Mutability and Immutability
* Object has type, state and it is located in specific address in memory (Python's heap)
* Ability to mutate the object is called mutability
* Not being able to mutate the object is called immutability
* Mutate - Changing the state of the object without changing the memory address
* Examples
    * Immutable Types: int, float, bool, complex, string, tuple, frozenset
    * Mutable Types: Lists, Dictionary, Set
* Immutable objects generally do not have side effects (which make them safe)

---

# Shared References, Mutablity and Pass by Reference
* Shared reference
    * Two or more variable pointing to same object
    * Function: All arguments in Python are pass by reference
    * Pass by Reference: The memory address of variable is passed rather than the value
* Take care your code from unintended side effects in function
    * Passing mutable objects to a function
    * Immutable objects containing mutable objects

---

# Objects and Equality
* Identity operators: is, is not
    * Whether or not two objects same
    * Variables point to object in same memory location
    * Like us having two names (one in office and another at home)
* Equality operators: ==, !=
    * Whether or not both objects are in same state
* If object1 is object2, then object1 == object2
* If object1 == object2, then object1 is object2 need not be true
* If object1 != objects, then object is not object2

---

# NoneType
* Usually, "None" (without double quotes) denotes an object does not have any value
* None is actually an object
* Type of None is NoneType

---

# Python Optimizations
* Integer interning (-5 to 256)
* String interning (identifier like objects are interned)
* sys.intern to intern strings
* Peephole optimizations
    * Constants expressions are optimized at compile time
    * Short sequences lesser than 20 are interned
    * Mutable types are replaced by immutable types when mutable types are used in membership tests
        * list to tuple
        * set to frozenset
    * my_func.\_\_code\_\_.co_consts
* Membership tests of set is much faster than lists/tuple

---

# Exercises 

---

layout: true
class: center, middle, inverse

---

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)