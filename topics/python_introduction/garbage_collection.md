name: inverse
layout: true
class: center, middle, inverse

---

# Garbage Collection
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false


# Reference
- Assigning an object to a variable and making it to point to the object
- It is actual link or connection made

---

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

---

# Garbage Collection
 - Python remembers the reference count
 - When reference count reaches "zero", the object is delete and GC reclaims the memory
 - Python handles circular references
 - Can be controlled using "gc" module
 - GC can be turned off (but do not do it)
 - Runs periodically
 - You can run GC

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