<!-- $theme: default -->

# Introduction to Python
## [GeeksHub](www.geekshub.in)
### [info@geekshub.in](info@geekshub.in)

---

# Agenda
- Introduction
	- What is Python?
	- Why to learn Python?
	- Properties of Python
	- Python Installation
- Baby Steps
	- Simple Input/Output
	- Variables
- Writing Comments
- References and Garbage Collection
	

---

# What is Python?
- [Language standard](https://docs.python.org/3/reference/)
- Python Compiler
- Converts the source code to bytecode (Python source to Python bytecode)
- Python Virtual Machine (PVM) or Python runtime - interpreter and Python Virtual Machine
  	- Loads the bytecode
    - Interprets the bytecode
    - Performs actions

---

# Why Learn Python (1/2)

- _**Expressive**_ language (like a poem). 
- Easy to learn
- Popular and hot market needs for Python developers
- Python has made inroads into a lot of areas
	- Web development, cloud development, automation, data analytics, artificial intelligence
- Increased productivity


---
# Why Learn Python (2/2)
- Increased Quality
- Community support. You will never be stranded. The community is there to help you.
- Lots of materials/books/videos from experienced developers
- Python is portable as Python code gets compiled to bytecode
- Libraries are vast and keeps growing. There is always some time-tested third party software available

---

# How to Learn Python
-

---

# Properties of Python
* Dynamic typing
  - You do not need to declare any variable/reference beforehand
* Python detects types implicitly
  - Python detects the type of the object automatically
* Strongly typed 
	* You cannot mix objects. For example, cannot add an integer with a string
* Case sensitive

---

# Setting up Python

- Windows, Linux (different flavors), MacOS
  - Available on most platforms
  - We will deal with CPython
- PyCharm, Atom, Visual Studio Code
  - Visual Studio Code is pretty decent
  - Atom or Sublime is equally good
  - PyCharm is an IDE (there is a free version too)
- Python Shell, IDLE
  - Use this if you want to try something quickly
  - Ok to use during initial days of learning Python
  - But soon move to standard editors

---

# Simple Input

---

# Simple Output

---

# Variables
 - It is the name given to an object
 - It is an alias referring to an object
 - Very much like human having names, some of us have an official name at school/college/office and probably another name at home. But still the same person

# Variable - Rules
* starts with _ (underscore), alphabet
* followed by _, alphabet, numbers
* cannot be keywords or reserved words

---

# Variable - Convention
* Variable starts with understand indicates "private" object
* Variable starts with dunder - Mangle class attributes
* Variable starts with dunder and ends with dunder
	- System defined names
    - Do not reinvent
    - Live with Python provided by using predefined names given by Python
    
---

* PEP8 - Code Style Guide
    * Packages - short, all lowercase, no underscores
    * Modules - short, all lowercase, underscores are allowed
    * Classes - CamelCase
    * Functions - snake_case
    * Variables - snake_case
    * Constants - IP_ADDRESS, PORT_NUMBER, CUSTOMER_ID
    
---

# Reference

- Assigning an object to a variable and making it to point to the object
- It is actual link or connection made

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

# Comments

---

# Multiline Statements

---

# Helping yourself

---

# 