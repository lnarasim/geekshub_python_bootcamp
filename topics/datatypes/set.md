layout: true
class: center, middle, inverse

---

# Set and Frozen Set
with [examples](set.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Properties of Sets
  - Similar to sets in Set theory
  - collection of unique/distinct object
  - No duplicates
  - Unordered
  - Object in the set can be of different types
  - Immutable types can only be added to the set. Mutable types cannot be added to the set.
  - Does not support indexing or slicing

---

# Creating set
  - use set()
  - use set(<iterable object>) - String, List, tuple can be 
    passed
  - set can be defined using braces
      ```python
            s = {1,3,4,5,6}
      ```
      
---

# Operators:
  - len() - to know the size
  - in or not in - to know whether an object exists in the set 
  - | (pipe), performs the union operation
  - &, performs the intersection
  - -, performs the difference
  - ^, symmetric difference (set of elements in either one of the sets but not in both)
  - <=, performs subset
  - \>=, performs superset
  - <, performs proper subset
  - \>, performs proper superset
  - |=, performs set.update()
  - &=, performs set.intersection_update()
  - -=, performs set.difference_update()
  - ^=, performs set.symmetric_difference_update()

---

# Methods:
   - set.add()
      - adds an object/element to the set 
   - set.remove()
      - removes the object from the set
   - set.pop()
      - removes and returns the object from the set
   - set.discard()
      - removes the element from the set if exists, otherwise do nothing
   - set.clear(), clears the set.
   - set.union(), set.intersection(), set.difference()
     set.symmetric_difference(), set.issubset(), set.issuperset()
      * same as given before. Instead of symbol, the respective
          methods can be used
   - set.disjoint()
        * True if there are no common elements, else False
   - set.update()
   - set.intersection_update()
   - set.difference_update()
   - set.symmetric_difference_update()

---

# Frozen sets:
- Similar to set
- But IMMUTABLE

---

# Exercises

1. Define two sets and perform the following.
        - intersection
        - union
        - difference

2. Create an empty list, tuple and set

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---
