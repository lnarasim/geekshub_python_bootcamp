layout: true
class: center, middle, inverse

---

# Packing & Unpacking
with [examples](packing_unpacking.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Packing and Unpacking - Basics
- Packing
    - Values that are bundled together
    - Ex: Tuples, lists, strings, sets, dictionaries
- Unpacking
    - Splitting packed values into individual variables
    - Order is not guaranteed when unpacking unordered types
    - Unpacking works for any iterable types
    - Right Hand Side is evaluated first
    - Number of variables in LHS should equals number of items in RHS

---

# Extended Unpacking
- Use * to mention variable number of items
- Works on any iterable
- Unpacks as list
- * can be used only once in LHS
- * in RHS is used to unpack all items in iterable
- Can be nested

---

# Let us see examples

---

# Exercises

1. You have a set, a list, a tuple. Create a list that has all items

2. Remove duplicate from the above list

3. You have a dictionary containing name, age and address. Unpack and print it as key value pairs

4. Swap two variables

5. Write down how unpacking is done

6. Write down how extended unpacking is done

7. Prove that ordering is on guaranteed while unpacking

---

# Exercises (cntd)

8. What will be the output of the following statements
    ```python
    lst = [1, 2, 3, [4, 5, [6, 7]]]
    a, b, *c, (d, *e) = lst
    ```

9. What will be the output of the following statements
    ```python
    d1 = {'key1': 1, 'key2': 2}
    d2 = {'key2': 3, 'key4': 4}

    d = {*d1, *d2}
    print(d) # a set of keys
    ```

---

# Exercises (cntd)

10. What will be the output of the following statements
    ```python
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    s3 = {5, 6, 7}
    s4 = {7, 8, 9}

    s = {*s1, *s2, *s3, *s4}
    print(s)

    l = [*s1, *s2, *s3, *s4]
    print(l)
    ```

11. What will be the output of the following statements

    ```python
    a, b, *c, d = 'python'

    print(a)
    print(b)
    print(c)
    print(d)
    ```
---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---