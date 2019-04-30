layout: true
class: center, middle, inverse

---

# Partial Functions
with [examples](partial_functions.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Reducing Function
* Reducing the number of arguments passed to a function
* Passing pre-determined value

# functools.partial
* partial(fn, args)
* Example: 
    * sq = partial(power, 2)
    * cube = partial(power, 3)
* Arguments memory location is baked into partial function.
* Arguments can be changed (using named arguments)
* If arguments passed is mutable (like list), the list can be changed

---

# Exercises

* Write a program to sort a given (x, y) co-ordinates based on the distance from the origin (0, 0)

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---