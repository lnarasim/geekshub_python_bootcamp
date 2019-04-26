layout: true
class: center, middle, inverse

---

# Closures
with [examples](closures.ipynb)
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
* Scopes - global, local, nonlocal

---

# What is Free Variable?
* Let us see an example first
    ```python
    def outer():
    lstx = [1, 2, 3]
    lsty = [4, 5,6 ]
    print("outer:", lstx, lsty)
    print("outer:", hex(id(lstx)), hex(id(lsty)))
    def inner():
        nonlocal lsty
        lsty = [10, 20, 30]
        print("inner:", lstx, lsty)
        print("inner:", hex(id(lstx)), hex(id(lsty)))

    inner()
    
    print("outer:", lstx, lsty)
    print("outer:", hex(id(lstx)), hex(id(lsty)))

    print("free_vars:", inner.__code__.co_freevars)

    outer()

    ```

---

# Free Variable - Example
* A function "outer" is defined
* outer has two local variables pointing to lists
* "outer" is created when def outer() is executed
* "outer" is evaluated when outer is called
* "inner" is created when outer is called
* The binding of nonlocal variables in "inner" happens when "inner" is created
* lstx and lsty are free variables

---

# Closure - An Example
* Let us see an example first
    ```python
    def outer():
    lstx = [1, 2, 3]
    lsty = [4, 5,6 ]
    print("outer:", lstx, lsty)
    print("outer:", hex(id(lstx)), hex(id(lsty)))
    def inner():
        nonlocal lsty
        lsty = [10, 20, 30]
        print("inner:", lstx, lsty)
        print("inner:", hex(id(lstx)), hex(id(lsty)))
    
    print("outer:", lstx, lsty)
    print("outer:", hex(id(lstx)), hex(id(lsty)))
    print("free_vars:", inner.__code__.co_freevars)
    
    return inner

    f = outer()
    print("global:", f.__name__)
    print("global:", f.__closure__)
    print("global:", f.__code__.co_freevars)
    ```

---

# Closure
* An inner function along with its free variables
* Binding of free variables happens when inner function is created
* Evaluating of free variables happens when inner/closure is called
* Free variables are accessed using Python cells
* Cell address of a free variable cannot change
* The object pointed by cell can change when the closure is called
* Every time outer fn is created, a new closure is created, new cells are created

---

# Sharing Extended Scopes
* Example
    ```python
    def outer():
        count = 0
        
        def inc1():
            nonlocal count
            count += 1
            return count
        
        def inc2():
            nonlocal count
            count += 1
            return count
        
    return inc1, inc2

    f1, f2 = outer()

    print(f1.__code__.co_freevars, f2.__code__.co_freevars)
    print(f1.__closure__, f2.__closure__)
    print(f1())
    print(f2())
    print(f1())
    print(f2())
    ```

---

# Beware: Sharing Extended Scopes with lambda
* What will happen here?
    ```python
    def outer():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
        
    return adders

    lambda_adders = outer()
    print(lambda_adders)
    print(lambda_adders[0](5))
    print(lambda_adders[1](5))
    print(lambda_adders[2](5))
    ```

---

# Nested Closure
* Let us see an example
```python

    # Nested closure
    def incrementer(n):
        def inner(start):
            current = start
            def inc():
                nonlocal current
                current += n
                return current
            return inc
        return inner

    fn = incrementer(3)
    inc_by_3 = fn(1)

    for _ in range(10):
        print(inc_by_3(), end=" ")
```

---

# Exercises

1. Implement an incrementor using closure. The outer function should take two arguments (starting value and step) and should return an inner function which will actually increment. The increment (inner function) should increment every time it is called

2. Implement a simple timer.  The outer function should record start time. The inner function should return time elapsed whenever the inner function is called

3. Implement a simple iterator. Given a list to outer function, the itertor should return next element from the list.

4. Implement a Python program using closure to print the mathematical table (2nd table, 3rd table)

5. For all the above programs, print the values of \_\_closure\_\_ and free variables


---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---