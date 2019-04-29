layout: true
class: center, middle, inverse

---

# Lambda
with [examples](lambda.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Lambda
* Another way of creating simple function
* Anonymous function
* Can be assigned to a variable
* Then the variable can be called
* Syntax:

    ```python
    lambda [parameter list] : <expression evaluated and returned>
    ```
---

# Lambda (cntd)
* Single logical line, line continuation is fine
* returns the value of the expression
* Can give default values to parameters
* Can have positional params, keyword only params, variable positional params, variable keyword params
* Pretty much like function (without name and can have only expression)

---
# Lambda Limitations
* Limited to single expression
* No assignments allowed
* No annotations

---

# Lambda - Examples
* Let us see some examples
    ```python
    func1 = lambda x: x ** 2
    func1(3)

    func2 = lambda x, y: x + y
    func2(2, 3)

    func3 = lambda x, y, z: x + y - z
    func3(2, 3, 1)

    func4 = lambda x = 3, y = 4: x ** 2 + y ** 2 + 2 * x * y
    func4(3, 2)

    def apply_func(fn, *args):
        return fn(*args)
    print(apply_func(func1, 3))
    print(apply_func(func2, 2, 3))
    print(apply_func(func3, 2, 3, 1))
    print(apply_func(func4, 3, 2))
    ```
---

# Exercises

1. Write a lambda to calculate the area of a circle

2. Write a lambda to calculate the area of a square

3. Write a lambda to calcuate the area of a rectangle

4. Write a lambda to calcuate the area of a triangle

5. Write a lambda to check whether or not given string is a palindrome

6. Write a lambda to check whether or not given number is multiple of 3 and multiple of 7

7. Write a lambda that does not take any arguments but returns the current time

---

# Exercises (cntd)

8. Write a lambda that takes one positional arguments and variable number of positional arguments. Finds the sum of the arguments and returns it

9. Write a lambda that takes default values

10. Write a lambda that takes two keyword only arguments one with default values, another without defaults and print them all

11. Write  a lambda that takes positional arguments, variable positional arguments, keyword only args, variable keyword only args and print the arguments

12. Write a program using lambda that sorts of strings based on the length of the strings and returns a new list
        * Input: ['aaaa', 'aaa', 'b', 'aa']
        * Output: ['b', 'aa', 'aaa', 'aaaa']

---

# Exercises (cntd)

13. Write a program using lambda to sort a list of strings. The sorting should be case insensitive

14. A dictionary has a set of keys and values. The keys are names of the students and values are their average scores. Write a program using lambda that displays the names and scores of the students as tuples that are sorted based on scores (the highest score comes first)

15. Given a list of objects, randomize the list (using sorted and random.random())

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---