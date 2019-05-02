layout: true
class: center, middle, inverse

---

# Conditionals
with [examples](conditionals.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# if, elif, else conditionals
- if condition:
- if condition: ... else:
- if condition: ... elif condition: .. elif condition:
- if condition: ... elif condition: .. elif condition: ... else:
- elif and else are optional
- if conditionals can be nested

---

# Conditional Expression or Ternary
- Evaluate an expression using ternary operations
    ```python
    #"expression when true" if <condition> else "expression when false"

    b = "a > 20" if a > 20 else "a <= 20"
    ```
- Can be nested
    ```python
        a = 10
        b = 12
        c = 8
        greatest = a if a > b and a > c else b if b > c else c
    ```
---

# Exercises

1.  Write a program that checks whether a number is even. If it is even, just
    print that the number is even (ex: 2 is even, 4 is even)

2.  Write a program that checks whether a number is even or odd. Print a message
    that it is even or odd. For example, output should look like as follows
        - 2 is even
        - 3 is odd
        - 4 is even
        - 7 is odd

3.  Write a program that takes scores of five subjects as list. Calculate the
    average score and print the grade.
        - 0% to 34% - Fail
        - 35% to 59% - Second class
        - 60% to 74% - First class
        - greater than 75% - First class with distinction

---

# Exercises (cntd)

4.  Write a program to demonstrate various operations.
        - 5 == 5
        - 5 != 5
        - 5 > 5
        - 5 >= 5
        - 5 < 5
        - 5 <= 5
        - 5 is 5

5.  Write a program to find whether a given number is a multiple of 5 and also
    a multiple of 9.

6.  Write a program to find whether a given number is a multiple of 5 or a
    multiple of 9.

---

# Exercises (cntd)

7.  Write statements to find out whether the following expressions evaluate to
    True or False.
        - False
        - None
        - 0
        - 0.0
        - ''
        - []
        - ()
        - {}

8.  Read about the function 'id' and observe the output. What is the relation
    that it has with operator "is"

9.  Give examples to prove - if a is b, then id(a) equals id(b)

10. Give examples to prove - if a == b, then id(a) need not be equal to id(b)


---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---