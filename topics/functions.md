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

# Positional Parameters
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

# Default Values - Positional Parameters
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
* Positional argumentes with default values can be omitted by caller

---
# Calling a function with Arguments
* Arguments must be passed for all mandatory positional parameters
* Arguments that has default values defined can be omitted.
* If omitted, the function takes the default value
* Function can be called with named arguments.
* Order is not important when the arguments are named
* If arguments are named, all the arguments that follows should also be named

---

# Variable Length Positional Parameters
* After positional arguments, we can define *args as variable number of positional parameters
* After this, no positional arguments can be defined
* It works pretty much like packing
* Uses tuple
* Cannot assign default values can variable length can range from 0 to anything
* "*" (with parameter name) denotes end of positional arguments

---

# Keyword Only Parameters
* After positional arguments, we can define keyword only parameters
* The caller should use keyword name to pass the value and call the function
* Can take default values
* Caller can omit if default values are given

---

# Examples 

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

# Variable Length Keyword Parameters
* Like positional arguments, we can define variable length keyword parameters
* Interpreted as dictionary
* Represented as **kwargs by convention
* No parameters can be defined after **kwargs
* Can be called by caller in any order

---

# Function Definition - Revisit
- Any number of positional parameters
- *args (to denote variable number of parameters) or "*" (denotes end of positional arguments)
- Followed by any number of keyword parameters (you need to name them while calling)
- Followed by **kwargs
- Each of the parameters can have default value
- If default values are given, the caller can omit them while calling the function

---

# First Class Functions
* Passed to a function as argument
* A function can be returned
* It can be assigned to a variable
* Stored in a data structure
* Functions are first class citizens

# Higher Order Functions
* A function is called higher order function if
    * Takes function as argument
    * Returns a function

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

8. Write a function that computes factorial of a given number. Implement a cache that remembers the factorials that are already calculated.

9. Write a function that does not have return statement. Call the function and store the return value to a variable and print the variable. Find out what Python does when there is no return statement or nothing is returned

10. For the various parameters we say - positional, variable length positional parameters, keyword only parameters and variable length keyword only parameters, write a function to demonstrate all, document using annotations. Use help() to see your documentation

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---