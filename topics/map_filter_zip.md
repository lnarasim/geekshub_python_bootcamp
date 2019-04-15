layout: true
class: center, middle, inverse

---

# Map, Filter, Zip
with [examples](examples/map_filter_zip.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Map, Filter, Zip
* Higher order functions
* Map
    * Returns an iterator that calculates the function applied to each element of the iterables
    * map(fn, *iterables)

* Filter
    * Run and return an iterable when it satifies a condition
    * If function is None, it returns based on Truth value of the object

* Zip 
    * Returns an iteratble with each element of iterables as tuple

---

# Map - Examples
* Let us see an example
    ```python

    def total(*args):
        return sum(args)

    lyst1 = [1, 2, 3, 4, 5,]
    lyst2 = [10, 20, 30, 40, 50]
    lyst3 = [100, 200, 300, 400, 500]

    result = list(map(total, lyst1, lyst2, lyst3))
    print(result)

    result = list(map(lambda *args: sum(args), lyst1, lyst2, lyst3))
    print(result)

    result = list(map(lambda x, y: x + y, lyst1, lyst2))
    print(result)
    
    ```

---

# Filter - Examples
* Let us see some examples
    ```python
    lyst1 = [1, 2, 3, 4, 5,]
    lyst2 = [10, 20, 30, 40, 50]
    lyst3 = [100, 200, 300, 400, 500]

    def is_even(x):
        return x % 2 == 0

    result = list(filter(is_even, lyst1))
    print(result)

    result = list(filter(is_even, lyst2))
    print(result)

    result = list(filter(is_even, lyst3))
    print(result)

    result = list(filter(lambda x: x % 2 == 0, lyst1))
    print(result)

    lyst1 = [0, None, False, {}, {}, set(), tuple(), 1, True, (1, 2)]
    result = list(filter(None, lyst1))
    print(result)
    ```

---

# Zip - Examples
* Let us see some examples
```python
    lyst1 = [1, 2, 3, 4, 5,]
    lyst2 = [10, 20, 30, 40, 50]
    lyst3 = [100, 200, 300, 400, 500]

    result = list(zip(lyst1, lyst2, lyst3))
    print(result)

    result = list(zip(lyst1, lyst2, lyst3))
    for element in result:
        print(element)
        
    for a, b, c in result:
        print(a, b, c)
```

---

# Exercises (1/3)

1. Write a map to calcuate some of elements of two lists

2. Write a map to calcuate area of the rectangles. The lists "length" and "breadh" contains length and breadh of rectangles

3. There are three lists containing first name, middle name and last name of individuals. Write a map to evaluate full name of the individuals and store it in another lists named "full name"

4. There are arbitary number of lists. Write a map to caculate the the sum of elements of the lists. The map should work for any number of lists

5. For the following lists x, y, z. Perform x + y - z using map.
    - x = [1, 2, 3, 4, 5]
    - y = [10, 20, 30, 40, 50]
    - z = [100, 200, 300, 400, 500]

---

# Exercises (2/3)

6. For the following lists x, y. Perform square of (x + y) using map.
    - x = [1, 2, 3, 4, 5]
    - y = [10, 20, 30, 40, 50]
    - z = [100, 200, 300, 400, 500]

7. Perform all the above using lambda

8. Write a filter to get list of all prime numbers from 1 to 1000

9. Write a filter to get list of all numbers between 1 and 100 that are divisble by 7

10. Given a list of strings, write a filter to get list of strings that are palindrome

---

# Exercises (3/3)

11. Write a map/filter that finds some of elements that are divisble by 7. (Hint: You need to find a list with some of each elements of the lists and then get a list containing elements that are multiple of 7)

12. Try solving the previous example with lambda

13. You have a list of lists representing a square matrix. Write a zip function to transpose the matrix

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---