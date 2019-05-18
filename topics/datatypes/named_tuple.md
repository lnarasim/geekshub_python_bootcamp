layout: true
class: center, middle, inverse

---

# Named Tuple
with [examples](named_tuple.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Named Tuples
* Using tuple as data record, accessing by position index might be confusing
* Alternates
    * Classes (implement repr and eq), classes are still mutable
    * Named tuple
* Named Tuple
    * Attach meaningful names to positions
    * Subclass of tuple
    * "namedtuple" is a function that generates a new class

---

# How to create Named Tuple
* Classname
* fieldnames in the order of elements
    * Valid variable but without underscore
    * Autogenerates field names
    * a list of strings, a tuple of strings, a string separated by white spaces
* Creates and Returns a class object
* Use returned class like normal class
* Introspection: Class._fields

---

# Accessing Named Tuple
* By Index
* By Slicing
* By Iteration
* By Names
* Unpacking and Extended Unpacking

---

# Other features of Named Tuple
* _asdict
* _make
* _replace
* Extending named tuple
* docstrings
* default values - prototype, \_\_defaults\_\_
* Using named tuple as dictionary and class replacements (immutable requirements)

---

# Exercises

WIP

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---