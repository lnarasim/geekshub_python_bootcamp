layout: true
class: center, middle, inverse

---

# Loops
with [examples](loops.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# while
* Execute a block of code when a condition is True
* Repeat till the condition is True
* Exit out of the loop when the condition becomes False
* While has optional else block
* else block run when "while" loop exits normally
      * Does not run when the control exits out of the loop using break
* Python does not have do...while

---

# break and continue

* break
   - terminates for or while loop

* continue
   - skips the current iteration and goes to the starting of the loop

* break/continue inside try block
   * Always executes "finally" block even if there is a break/continue
    ```python
      a = 1
      b = 0
      while True:
            try:
                  a/b
            except ZeroDivisionError:
                  print("divide by zero error")
                  break
            finally:
                  print("This always gets executed")
      ```

---

* for loop
   - for iterates over iterable objects
   - Not same as while loop
   - iterable is object that is capable of returning values one at a time
      ```python
      for i in range(5):
      for element in [1, 2, 3, 4, 5]: # elements is a list
      for character in "Hello": 
      for element in (1,2,3,4,5):
      for tup in [(1,2), (3,4), (5,6)]:
      for a, b in [(1,2), (3,4), (5,6)] # with unpacking
      for index, element in enumerate([1, 2, 3, 4, 5])
      ```
   - break/continue/else works similar to while loop
   - finally executes even when there is a break or continue in a try..except..finally
   
---

# Exercises

1. Define a list that has numbers from 1 to 100 and print them using "for" loop. You have to use iteration using "for" and "in"

2. Repeat the previous problem of printing numbers producing the following output.
      - print numbers from 1 to 100 (both inclusive)
      - print all odd numbers between 1 and 100 (both inclusive)
      - print all even numbers between 1 and 100 (both inclusive)
      - print all numbers between 1 and 100 that are multiple of 5
      - print all the numbers between 1 and 100 that are multiple of 5 but printing them in reverse order (100, 95, 90, .....)

3. Write a program the perform linear search (finding a number in a list of numbers). You should use break to exit after you find it first in the list

4. Write a program to find number of times that a number exists in the list assuming that the number is present more than one time.

---

# Exercises

5. Python has built-in function for sorting. But without using it, write a function to sort the list in ascending order. (you will learn nested "for" loop in this)

6. Implement the previous program using while loop.

7. Write a program that never exits (You need write an infinite loop)

8. Write a program to illustrate "break" and "continue" with loops (do it for both "for" and "while" loops)

9. Write down what the following will do.
      - range(100)
      - range(1, 100, 3)
      - range(100, 1000, 10)
      - range(10000, 1000000, 100)

---

# Exercises


10. Write a function that takes a number and print the table. For example,
      - an input "2", print 2-tables
      - an input "3", print 3-tables
      - an input "5", print 5-tables

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---