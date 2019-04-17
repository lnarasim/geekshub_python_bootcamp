layout: true
class: center, middle, inverse

---

# List
with [examples](list.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false


# Lists in Python
- List, as name suggests, is a list of objects
- Similar to array. Unlike array, they can store heterogenous types
- Comma separate objects within a square bracket
    * Ex: [1, 2, 3, 4, 5, 6]
- Accessed by index numbers[0], numbers[2]
- Indexing starts from 0
- Join two lists using +
- Repeat lists using *
- Lists can be nested (list can contain lists and each list can contain lists. It can be chained to any level)
- List can have dictionary, dictionary can have lists

---

# Lists properties
* Ordered (insertion order)
* Unlimited number of objects
* Can grow or shrink
* Mutable

---

# Slicing (similar to String)
* Start index (begins from zeroth index if not specified)
* End index (ends at last index if not specified)
* Step (defaults to 1 if not specified)
* start index, end index and step can be negative

---

# Membership Operators
- in operator
- not in operator

---

# List operations
- Modify single value such as a[0] = 1
- Modify multiple values such as [2:3] = [1,2,3]
- Removing an element from the list
    * del a[0]
    * del a[1:]
    * del a[:]
    * Assigning empty list a[1:5] = [] to remove elements from 1 to 4

---

# List Functions
- list.append()
    * Adds an object to the end of the list
- list.extend()
    * append the list with iterable object
- list.insert()
    * inserts object at specific index
- list.remove()
    * removes the specified object from the list
- list.pop()
    * removes and returns the last element of the list

---

# Comprehensions
- Powerful
- An expression that works on the list elements
- They produce a list

---

# Exercises 

1. Define a list of states in your country and print the list (this is going to be Python list. Something like this states = ["TN", "KA", "KL", "AP", "MP"])

2. Define the list and print the element at the following position (position different than index. Index is a number lesser than the position by 1)
    - first element in the list
    - second element in the list
    - third element in the list
    - last element of the list
    - the value at last but one
    - print the index of a value in the list that is existing
    - print the index of a value that is not in the list
    - print the length of the list
    - print the first and second element of the list
    - print the first five elements of the list.
    - print the third and fourth element of the list.

---

# Exercises (Cntd)

3. Add an element to the list by the following methods
    - add an element to the end of the list.
    - add an element at zeroth index.
    - add an element at fifth index.

4. Define the following lists
    - list of districts in your state.
    - list of districts in your neighboring states with each of the neighboring state in a separate list.
    - create a list called "states" and add all the lists created above to list "states". So, this will be a list containing lists

5.  Define two lists and add all the elements of second list to the first. For example, if first = [1, 2, 3, 4, 5] and second = [6, 7, 8, 9, 10], the output should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

---

# Exercises (Cntd)

5. Define two lists and add the elements of both list to another common list. Ensure that first and second list should not be altered.

6. Remove an element from the list (use remove function)

7. Remove the element from the list (using pop function)

9. What is the difference between remove and pop?

10. Reverse a list

11. Sort a list using sort function
    - ascending order
    - descending order
    - Repeat for the list that has alphanumeric values
    - Repeat for the list that has int values
    - Repeat for the list that has float values

---

# Exercises (Cntd)

12. Repeat the above sorting exercise without changing the original list.

13. Find the index of 5 in the following lists
    - first = [1, 2, 3, 4, 5]
    - second = [1, 2, 3, 4]

14. Find whether an element/value present in a list.

15. Define a list and loop through it. Print the value at each index.

16. Define a list and loop through it. Print the value at each index along with index value

17. Define a list and loop through it. Print the value at each index along with index values and the index value should start from 1

18. Create a list of names of your friends. Create a friendship string with names of your friends separated by comma. For example, if the list is friends = ["Ram", "Krishna"], the output should be "Ram, Krishna"

---

# Exercises (Cntd)

19. Take the friendship string (output of previous problem) and convert it back to string using split

20. From the list "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", perform the following and get a new list.
    - a list containing first two elements
    - a list contain elements from third position to sixth position
    - a list containing last two elements
    - a list containing sixth and seventh position
    - a list contain elements from first to last but one
    - a list containing last four elements
    - a list containing first and last elements

21. A square matrix N*N is expressed as list. Write a function that calculates the sum of diagonal elements. Note that there will be two diagonals in a square matrix.

22. A list contains many elements of the types. Write a function that creates a separate lists for integer, float, string and everything else.

---

# Exercises (Cntd)

23. Given a list, how will you clear all the elements of the list. For example, numbers = [1,3,3,4,6,6] should be converted to numbers = [] without creating a new instance of an empty list (id(numbers) before and after the transformation should be same)

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---