layout: true
class: center, middle, inverse

---

# Reducing Functions
with [examples](reducing_functions.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Reducing Functions
* Process all the items in iterable and return single value
* Accumulators, aggregators, folding functions
* Examples
    * Maximum value in a sequence
    * Minimum value in a sequence
    * Sum of all numbers in a sequence
    * Product of all numbers in a sequence
* Built-in reducing functions - min, max, sum, any, all

---

# functools.reduce
* Works on any iterables
* Pass a function (or a lambda) that works on the iterable
* Returns one value
* Optionally pass an initializer (initial value)

---

# Exercises

1. Write a program to find the maximum value in a given sequence sequence of numbers

2. Write a program to find the minimum value in a given sequence of numbers

3. Write a program to add all the value in a given sequence of numbers

4. Write a program to concatenate all the strings in a given sequence of strings

5. Write a program to find the product of all numbers in a given sequence of numbers

6. Implement a function "my_any" that takes a sequence as argument and returns True if at least of the element evaluates to True and False if all the element evaluate to False. (Note: Every object has a truth value)

---

# Exercises (cntd)

7. Implement a function "my_all" that takes a sequence as argument and returns True if all the elements evaluates to True and False if at least one of the elements evaluates to False. (Note: Every object has a truth value)

6. Write a generic funtion that takes function and sequence as arguments and returns the reduce function

7. Implement all above exercises using functools.reduce passing lambda function

8. Read help of the following functions and do some examples
    * min
    * max
    * sum
    * any
    * all

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---