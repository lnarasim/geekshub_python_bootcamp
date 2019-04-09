layout: true
class: center, middle, inverse

---

# Datatype - bool
with [examples](examples/bool.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Boolean
* Two values - __True__ or __False__
* bool is a subclass of int
* True and False are singleton objects
* All operations that can be performed on int can be performed on bool
* [PEP 285](https://www.python.org/dev/peps/pep-0285/)

---

# Truth value
* All objects in Python has a truth value
* All objects by default "True"
* Truth value is determined by bool()
* Examples:
```python
      bool(True)
      bool(False)
      bool(10)
      bool([])
      bool('hello')
      bool(None)
```
* \_\_bool\_\_ and \_\_len\_\_ methods convey truth value
   * \_\_bool\_\_ determines truth value
   * \_\_len\_\_ determines truth value if \_\_bool\_\_ not present
   * True if both \_\_bool\_\_ and \_\len\_\_ not present
---

# bool is an int
* bool is subclass of int
```python
      a = False
      isinstance(a, bool)

      a = False
      isinstance(a, int)
```
* All operations can be performed
   - True + True + True (equals three)
   - True > False (evaluates to True)
   - (1 == 2) == False (evaluates to True)
   - (1 == 2) == 0 (evaluates to True)
   - -True == -1 (evaluates to True)
* int(1) and True are equal but int(1) is not True
* int(0) and False are equal but int(0) is not False

---
# Objects Truth Value
* Objects having False truth value
   - None
   - False
   - 0 (int, float, decimal, complex, fraction)
   - '' (empty string)
   - [] (empty list)
   - set() (empty list)
   - {} (empty dictionary)
   - Customer classes that defines False value using \_\_bool\_\_ or \_\_len\_\_
* All other scenarios, objects considered True

---

# bool() evaluations
* bool(0) -> False
* bool(1) -> True
* bool(-1) -> True
* bool(100) -> True
* bool(None) -> False
* bool('') -> False
* bool([]) -> False
* bool({}) -> False
* bool('something') -> True
* bool([1]) -> True
* bool({'key': 1}) -> True

---

# Boolean Operators
* not
  - True if False, False if True
  - Unary operator
* and
  - True if both True, else False
  - Binary operator
* or
  - True if either one is True, else False
  - Binary operator

---

# Operators and Precedence
* ()
* <, \>, <=, >=, ==, !=, in, is
* not
* and
* or

---

# Short Circuit
* x or y -> if x is True return x else return y
* x and y -> if x is False return x else return y
* Does not process if there is a short circuit
* Note that it returns actually object
* Python applies/calls \_\_bool\_\_ implicitly in if statements

---

# Chained Comparisions
* a < b < c equivalent to (a < b) and (b < c)
* a < b > c equivalent to (a < b) and (b > c)
* a < b in [1, 2, 3] equivalent to (a < b) and (b in [1,2,3])

---

### Beware of boolean, it can sometimes be overwhelming

---

# Exercises

1. Define a variable to point to True (say a)

2. Define a variable to point to False (say b)

3. Find id and type of a

4. Find id and type of b

5. Try really long short-circuiting with "or"

6. Try really long short-circuiting with "and"

7. Assign a variable "a" with an integer value of 0 (zero). Compare the truth value of int(0) with float(0), decimal(0,0), fraction(0,0) and complex(0, 0)

8. Repeat previous exercises for a value of 1, -1, -100, -5000

---

# Exercises (Cntd)

9. Try out few chained comparisons and have solid understanding on how it works (with short-circuiting)

10. Execute the examples given and write your observations

11. Try out empty mappings, collections and find their truth value

12. Implement \_\_bool\_\_ in one of your class and check out the truth value

13. Implement \_\_len\_\_ in one of your class and check out the truth value

---

# Exercises (Cntd)

14. What do the following statements evaluate to:
      - 3 < 4
      - id(3 < 4)
      - type(5 > 6)
      - None is False
      - None is True
      - (1 == 2) is False
      - int(True)
      - int(False)
      - 100 * False
      - -True
      - True + True + True
      - -True
      - a = 10, a.\_\_bool\_\_()
      - [].\_\_len\_\_()
      - [].\_\_len\_\_().\_\_bool\_\_()
      - [1].\_\_len\_\_().\_\_bool\_\_()

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---