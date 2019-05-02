layout: true
class: center, middle, inverse

---

# Datatypes
with [examples](datatypes.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# What is datatype?
* What kind of data?
* Where it is stored?
* How it is stored?
* How it is accessed?
* Can I modify it?
* Can I read?
* Is it thread-safe?

---

# Objects
* Everything is object in Python
* An object is memory location that contains some attributes and perform some behaviors
* We will deal with objects in detail later

# Types
* Built-in to Python
* User defined (rather developer defined)

---

# Type of Types (1/2)
* Numbers
    * Integral
        * integer
        * bool
    * Non-integral
        * float
        * Complex
        * Decimals
        * Fractions
* Collections
    - Sequences - list, strings, tuple
    - Sets - Set and FrozenSet
    - Mapping - dictionary
    - Mutable and immutable
* Callables
    - Functions, Generators, Classes
    - Instance Methods, Class instances, 
    - Builtin functions
    - Built-in methods
* Singleton
    - None, NotImplemented, Ellipsis

---

# Type of Types (2/2)
* Program unit types
    - Funtions, Modules, Classes
* Implementation related types
    - Compiled code
    - stack tracebacks

---

# Advantages of Built-in types
* Makes programs easy to write (compared to programming in C, where you need define, declare and manage the memory)
* Components of extensions
* Efficient
* Part of the language

---

# Dynamic Typing & Strongly Typed
* Variables do not have fixed type
* "type" is stored in object not with variable name
* Variables are names given to object
* They can point to different objects at different times
* Python detects types automatically
* Types live in objects (not in variable names)
* Strongly Typed
    * A type can do what is defined in its class
    * A list object can perform only list operations, a dictionary can perform only dictionary operations

---

# Mutable and Immutable
* Mutable
    - Inplace modification is allowed (ex: Insertion of new element should be allowed)
    - Interal state of the object can be changed
    - Might lead to unintended side effects

* Immutable 
    - Inplace modification is not allowed
    - Internal state of the object cannot be changed
    - Warning: Immutable objects that has mutable composition still have side effects

---

layout: true
class: center, middle, inverse

---

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)