layout: true
class: center, middle, inverse

---

# Functions
with [examples](examples/functions.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Functions
* Principles
    * Code Resuabilty
    * Separation of Concern
* Variables and scope
    * Local Variables (vs Module Scope)
    * Pass by Reference
* Arguments (we call them arguments when calling a function)
* Parameters (we call them parameters when defining a function)
* Functions are objects
    ```python
    def something():
        pass
    type(something)

    >>> type(something)
    <class 'function'>
    >>>
    ```

---

# Defining a Function
* A function is defined using keyword "def"
* Followed by zero or more number of parameters
* Returns a value (one or more)
* An identation is necessary
    ```python
    def func():
        pass
    ```
* Call functions any number of times
    ```python
    func()
    ```
---

# Parameters
* Function can have one or more parameters
    ```python
    def func(a, b, c, d):
        print(a, b, c, d)

        return a, b

    func(1, 2, 3, 4)
    ```
* Each parameter has a position
    * a's position is 1, b's position 2, c's position is 3 and d's position is 4

---

# Default Values - Parameters
* Each parameter can have default values assigned (d = 100)
    ```python
    def func(a, b, c, d = 100):
        print(a, b, c, d)

    func(1, 2, 3, 4) # d takes 4
    func(1, 2, 3) # d takes default value of 100
    ```
    * If 'd' is passed, it takes the passed value. Else the default value

* Positional arguments without default values should come first
* Followed by positional arguments with default values 

---

# Keyword arguments
* While calling a function, arguments can be named
* Order is not important if arguments are named
* If arguments are named, all the arguments that follows should also be named
* Can be mixed with default values

---

# Keyword Arguments - Examples
* Some (interesting) examples
    ```python
        def func(a, b, c = 50, d = 100):
            print(a, b, c, d)

        # default values in action
        func(1, 2)
        func(1, 2, 3)
        func(1, 2, 3, 4)
        func(1) # should throw error
        func() # should throw error

        # named arguments in action
        func(1, 2, c = 3, d = 4)
        func(a = 1, b = 2, c = 3, d = 4)
        func(a = 1, 2, c = 3, d = 4) # this should throw error

        # named arguments and default values in action
        func(a = 1, b = 2)
        func(1, b = 2)
        func(1, b = 2, c = 150)

    ```

---
# Function Definition - Revisit
- Any number of positional parameters
- *args (to denote variable number of parameters)
- Followed by "*" (denotes end of positional arguments)
- Followed by any number of named parameters (you need to name them while calling)
- Followed by **kwargs

---

# Exercises

1. Write a function that returns list of numbers from 0 to 1000 that are multiples of 3 and 7

2. Given the radius of the circle, write a function to return area and circumference

3. Write a function that takes two arguments - that are sides of square or rectangle (say a and b). The second argument should be optional. The fuction should return area (a * b). But for the square it is enough to get length of a side.
    - area(a) should return a * a
    - area(a, b) should return a * b

4. Write a function to calculate compound interest if the principle, number of years, rate of interest is given. If not given, priciple should default to 1000, duration to 2  years and interest rate to 7%.

5. Calculate compound interest passing named arguments.

---

# Exercises (cntd)

6. Calculate compound interest passing named arguments in out of order (not preseving the order of definition)

7. Calculate compound interest without passing any arguments.

8. More to come

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---