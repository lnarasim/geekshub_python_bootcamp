layout: true
class: center, middle, inverse

---

# Function Introspection
with [examples](function_introspection.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Introspection
* Examining the code using code
* Functions are first class objects
* Similar to other objects, functions too have attributes
    * Ex: \_\_doc\_\_ and \_\_annotations\_\_
* We can add attributes to function
    * func.some_attribute = 10
---

# Function Attributes
* dir() - lists all attributes (similar to other objects)
* \_\_name\_\_ - name of the function
* \_\_defaults\_\_ - default values of positional params
* \_\_kwdefaults\_\_ - default values of keyword params
* \_\_code\_\_ - returns code object that contains various other information
    * co_varnames - parameters and local variables
    * co_argcount - Number of positional params excluding variable length positional params
    * co_kwonlyargcount - Number of keyword-only params excluding variable length keyword-only params

---
# inspect module
* isfunction() - True for function
* ismethod() - True for object's method
* isroutine() - True for both function and method
* inspect.getsource(func)
* inspect.getmodule(func)
    * inspect.getmodule(func)
    * inspect.getmodule(print)
    * inspect.getmodule(math.sin)
* inspect.getcomments(func)
    * gets the comment that is just above the function definition
    * Typically TODO is written above the function

---
# inspect.signatures
* inspect.signature - returns signature instance
    * Has parameters which is a dictionary
        * key is param name
        * values are attributes 
            * name
            * default
            * annotation
            * kind (positional, variable-pos, kwonly, var-kwonly)

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