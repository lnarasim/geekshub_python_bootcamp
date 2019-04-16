layout: true
class: center, middle, inverse

---

# Datatype - Float
with [examples](float.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Floats - General discussion
* Floats use fixed number of bits
* Python has an overhead of 24 bytes
* 64 bits
   - One sign bit
   - 11 exponent bits
   - 52 Significant bits
* Like ints, floats are signed in Python
* Limited precision
   * Some numbers can be represented using finite number of bits

---

# Floats in Python
* Integer is an object
* Immutable
* Limited in size
* It has overhead
* formating - format(20.1, '0.25f')

---
# Creating Floats
* a = 1.23
* float(10)
* float("10.0")
* float(fraction)
* float(decimal)

---
# Float airthmetic operations
* Addition
* Subtraction
* Multiplication
* Division
* Floor Division [(a = b * a // b) + a % b]
* Modulo [(a = b * a // b) + a % b]
* Exponent (or raised to the power)

---
# Some Math functions
* math.trunc()
* math.floor()
* Floor division vs math.trunc vs math.floor
* divmod
* bin, oct and hex

---

# Equality Testing Problems
* a = 0.1 + 0.1 + 0.1, b = 0.3. a == b fails
* Not Python's issue (floating point precision issue)
* Absolute tolerance
* Relative tolerance
* math.isclose


---


# Exercises (Cntd)

1. Define a variable pi and assign the value of pi. Print the value of pi (pi is a floating poing number)

2. Print type and id of the variable that points to pi

3. Assign a = 0.1 + 0.1 + 0.1 and b = 0.3. Find a == b. What do you observe?

4. Write a program that prints area and circumference of a circle for a given radius (try it having radius as integer and floating point)

5. Write a program to perform the following operations. Store the resultant value in a variable and print the variable with some meaningful text. For example, assign first = 2.1, second = 3.1 and print "2.1 + 3.1 = 5.2"
   - Addition
   - Subtraction
   - Multiplication
   - Division
   - Floor Division
   - Exponent or raised to the power
   - Modulus

---

# Exercises (Cntd)

6. Take two very large floats (probably 20 digits) and multiply both of them. Print the result.

6. Perform the following operations using the functions given. Read about these functions using help.
      - abs
      - round

7. Convert the following strings to int type using "float" functions
      - "2.0"
      - "100.0"
      - "-100.0"

8. Convert the following floats to int type using "int"
      - 2.0
      - 100.0
      - -100.0

---

# Exercises (Cntd)

9. Perform the following operators on integers and floating point numbers and print the result of evaluation (Note: either one of "True" or "False" should be printed. True or False is boolean values.)
      - 2.0 < 3.0
      - 2.0 > 3.0
      - 2.0 >= 3.0
      - 2.0 <= 3.0
      - 2.0 != 3.0
      - 2.0 == 3.0

10. Type the following code in your Python shell, find out the output
      ```python
      import math

      print(math.pi)
      print(math.sqrt(4))
      ```

---

# Exercises (Cntd)

11. What will be the output of the following when a = 100.1 and b = 100.2
      - math.isclose(a, b)
      - math.isclose(a, b, rel_tol=1e-9)
      - math.isclose(a, b, rel_tol=1e-2)
      - math.isclose(a, b, rel_tol=1e-1)

12. What will be the output of the following when a = 0.1 + 0.1 + 0.1 and b = 0.3
      - math.isclose(a, b)
      - math.isclose(a, b, rel_tol=1e-9)
      - math.isclose(a, b, rel_tol=1e-2)
      - math.isclose(a, b, rel_tol=1e-1)

---

# Exercises (Cntd)

13. What will be the output of the following when a = 12345.6789
      - round(a, -1)
      - round(a, -2)
      - round(a, -3)
      - round(a, -4)
      - round(a, -5)
      - round(a, 1)
      - round(a, 2)
      - round(a, 3)
      - round(a, 4)
      - round(a, 5)

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---