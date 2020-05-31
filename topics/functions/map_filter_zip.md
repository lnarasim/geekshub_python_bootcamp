layout: true
class: center, middle, inverse

---

# Map, Filter, Zip
with [examples](map_filter_zip.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Map
* Map and Filter are Higher order functions
* Map
    * Returns an iterator that calculates the function applied to each element of the iterables
    * Applies the function in parallel
    * Returns an iterator
    * Iterator stops as soon as at least one of the iterables is exhausted
    * map(fn, *iterables)

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

# Filter
* Filter
    * Determines whether to retain or throw the element from resultant iterator
    * Run and return an iterable when it satifies a condition
    * If function is None, it returns based on Truth value of the object
    * If functions returns True, the object is added to iterator
    * filter returns an iterator
    * filter(func, iterable)

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

# Zip
* Zip 
    * Returns an iteratble with each element of iterables as tuple
    * zip is not an higher order function
    * Stops at shortest iterable
    * zip(*iterables)

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

# Exercises

1. Write a map to calcuate some of elements of two lists

2. Write a map to calcuate area of the rectangles. The lists "length" and "breadh" contains length and breadh of rectangles

3. There are three lists containing first name, middle name and last name of individuals. Write a map to evaluate full name of the individuals and store it in another lists named "full name"

4. There are arbitary number of lists. Write a map to caculate the the sum of elements of the lists. The map should work for any number of lists

5. For the following lists x, y, z. Perform x + y - z using map.
    - x = [1, 2, 3, 4, 5]
    - y = [10, 20, 30, 40, 50]
    - z = [100, 200, 300, 400, 500]

---

# Exercises (cntd)

6. For the following lists x, y. Perform square of (x + y) using map.
    - x = [1, 2, 3, 4, 5]
    - y = [10, 20, 30, 40, 50]
    - z = [100, 200, 300, 400, 500]

7. Perform all the above using lambda

8. Write a filter to get list of all prime numbers from 1 to 1000

9. Write a filter to get list of all numbers between 1 and 100 that are divisble by 7

10. Given a list of strings, write a filter to get list of strings that are palindrome

---

# Exercises (cntd)

11. Write a map/filter that finds some of elements that are divisble by 7. (Hint: You need to find a list with some of each elements of the lists and then get a list containing elements that are multiple of 7)

12. Try solving the previous example with lambda

13. You have a list of lists representing a square matrix. Write a zip function to transpose the matrix

14. Given a list of radius of different circles, write a map to find out respective areas

15. Given a lists of length and breadh of rectangle, write a map to find out respective areas
    * length = [10, 20, 30, 40]
    * breadh = [2, 3, 4, 5]

---

# Exercises (cntd)

16. Given a list of tuples that represent the sides of rectangle or square, write a map/filter to get the list of tuples that defines rectangle
    * sides = [(10, 20), (2, 2), (3, 4), (4, 4)]
    * output should be [(10, 20), (3, 4)]

17. Given a list of tuples that represent the sides of rectangle or square, write a map/filter to get the list of tuples that defines square
    * sides = [(10, 20), (2, 2), (3, 4), (4, 4)]
    * output should be [(2, 2), (4, 4)]

18. Given three lists that has principle, number of years and interest rate, write a map/filter to calculate the compound interest.
    * principle = [1000, 2000, 4000, 5000]
    * years = [2, 4, 5, 6]
    * interest = [6, 7, 8, 9]
    * output should be [123.60000000000014, 621.5920200000005, 1877.3123072000026, 3385.500554205004]

19. Calculate simple interest for the previous problem using map/filter

---

# Exercises (cntd)

20. Write a simple zip function that returns the object in a list and respective index (mimic enumerate)

21. Take five strings of different sizes and write a zip function on those five strings.

22. What is the output of the following:
    ```python
    l1 = [1, 2, 3]
    l2 = []
    map(lambda x, y: x + y, l1, l2)

    ```
---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---