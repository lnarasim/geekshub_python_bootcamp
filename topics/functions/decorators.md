layout: true
class: center, middle, inverse

---

# Decorators
with [examples](decorators.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Functions - Refresher
* The functions are first class objects
* Passed to a function
* Returned from a function
* Can be stored in a data structure
* Can be assigned to a variable (and the variable can be used. 
```python
f = print, f(1, 2, 3))
```
* Functions can be nested

---

# Decorator
* It is a function that takes another function
* Extends the behavior of the function (decorates it)
* Does not modify the function

---

# Decorating - Steps
* Decorator takes a function as argument
* Wraps it inside another wrapper
* Returns a closure (wrapper)
* Overwrites actual function's label with wrapper
* Usually takes function with any number of arguments
* Returns the value returned by decorated function

---

# Let us do simple examples
1. Function with no args
2. Function with one args
3. Function with two args
4. Function with number of args
5. @
6. Function introspection
7. @wraps
8. Function introspection again

---

# Real World Use Cases
1. Decorating the log message
2. Debugging the code
3. Timing a function
4. Slowing down the code
5. Light weight replacement for classes

---

# Exercises

* WIP

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---