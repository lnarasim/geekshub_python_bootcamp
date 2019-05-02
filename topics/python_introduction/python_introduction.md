name: inverse
layout: true
class: center, middle, inverse

---

# Introduction to Python
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

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
- [Language Grammar](https://docs.python.org/3/reference/grammar.html)
- Python Compiler
   - Converts the source code to bytecode (Python source to Python bytecode)
- Python Virtual Machine (PVM)
  	- Loads the bytecode
   - Performs actions
- Python compiles and interprets your source code on the fly

---

# Why Learn Python (1/2)

- _**Expressive**_ language (like a poem). 
- _**Easy**_ to learn
- _**Popular**_ and hot market needs for Python developers
- Python has made inroads into a lot of areas
	- Web development, cloud development, automation, data analytics, artificial intelligence
- Increased _**productivity**_


---
# Why Learn Python (2/2)
- Increased _**Quality**_
- Community _**support**_. You will never be stranded. The community is there to help you.
- Lots of materials/books/videos from experienced developers
- Python is _**portable**_ as Python code gets compiled to bytecode
- Libraries are vast and keeps growing. There is always some _**time-tested third party software**_ available

---

# How to Learn Python
* Think before you code
* Code 
   * At least 1 hour if you are working, 
   * At least 4 hours if you are searching job
* Refactor
* Practice
* Write
* Help Others by teaching
* Review others code
* Do mini-projects

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
- Python Shell, IDLE
  - Use this if you want to try something quickly
  - Ok to use during initial days of learning Python
  - But soon move to standard editors
- PyCharm, Atom, Visual Studio Code
  - Visual Studio Code is pretty decent
  - Atom or Sublime is equally good
  - PyCharm is an IDE (there is a free version too)
- Setting up Jupyter
  - Install Jupyter
  - Install Jupyter themes

---
# Let Us Code
* Add two numbers
* Subtract a number from another number
* Multiply two numbers
* Try raised to the power
* Find the biggest number that can be stored in Python

---

# Simple Output
- "print"
- Formatted print (string.format)
- f-strings

---

# Simple Input
- "input"
- command-line args (import sys, sys.argv)

---

# Variables
 - It is the name given to an object
 - It is an alias referring to an object
 - Very much like human having names, some of us have an official name at school/college/office and probably another name at home. But still the same person

---

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

# PEP8 - Code Style Guide
* Packages - short, all lowercase, no underscores
   * fractions, decimal, math
* Modules - short, all lowercase, underscores are allowed
* Classes - CamelCase
   * BankAccount, EmployeeDetails
* Functions - snake_case
   * deposit(), get_employee_details(), write_to_db()
* Variables - snake_case
   * temperature_far, temperature_cel
* Constants - ALL CAPS
   * IP_ADDRESS, PORT_NUMBER, CUSTOMER_ID
    
---

# Comments
* Anything that comes after # is comment
* Considered comment from # to end of line
* Comments are stripped off during compilation

---

# String
* Text written between single quotes
* Text written between double quotes
* Examples:
   ```python
   greeting = "Hello"
   user = 'Lakshmi'
   ```
---

# Multiline String
* Text written between two triple double quotes
* Text written between two triple single quotes
* Standard string object
* Compiled in by the compiler
* These are not comments
* Use any operations that is supported in string (like format, formatted string)
* Commonly used for Docstring

---

# Multiline Statements
* Physical lines of code
* Logical lines of code
* Implicit line continuation (lists, tuples, sets, dictionaries, function parameters and arguments)
   * Can span across multiple lines
   * Supports inline comments
   * Ensure that you dont accidently comment a valid code
      ```python
      l = [1, 2 #item2, 
            3, 4 #item4]
      ```
* Explicit line continuation (use \\)
   * Use \\ to denote the line is continuing to next line
   * Does not support inline comments

---

# Helping yourself
* dir()
* help()
* Python documentation

---

# Exercises (1/3)

1. Install Python in your desktop/laptop

2. Try running few Python code using Python shell

3. Try running few Python script file "ex1.py", "ex2.py"

4. Download code editor such as Visual Studio Code or Atom. Use it for your development purpose

5. Explore the documentation of print function using help(print)

6. Explore the documentation of input function using help(input)

7. Explore the documentation of help function using help(help)

8. Explore the documentation of dir function using help(dir)

---

# Exercises (2/3)

9. Explore dir(help), dir(dir), dir(print), dir(input)

10. Print the following words using print function.
   - Hello, World
   - Python is Awesome
   - Today is Sunday
   - I will work in Python everyday
   - I will become expert in Python
   - Consistency is the key
   - I will improve myself everyday, every week

11. Get the name of the user, print the following.
   - Hi, <name>
   - How are you doing?
   - See you later, <name>

12. Install Jupyter Notebook and use it for daily practice

---
# Exercises (3/3)

13. Explore [www.python.org](www.python.org)

14. What are various flavors of Python available?

15. Write a paragraph about couple of the flavors?

16. Who is creator of Python?

17. Read about PEP. Read about couple of PEPs

18. Find out list of famous packages of Python for Data Science

19. Find out list of famous packages of Python for Machine Learning

20. Find out list of famous REST/Web frameworks

# 

---

layout: true
class: center, middle, inverse

---

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)