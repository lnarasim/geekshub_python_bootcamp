layout: true
class: center, middle, inverse

---

# String
with [examples](examples/string.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# String in Python
- String is one of the basic data types in Python. 
- String is a _sequence_ of one character string. 
- String is immutable.
    - When we perform an operation on string, it always produces a new object (Inplace modification is not allowed)
- String interning
    - Certain strings are optimized

---

# String - Some Examples

* Define a string
```python
greeting = "Hello"
```

* Define another string
```python
friend = "Guru"
```

* Add two strings
```python
greet_a_friend = greeting + ', ' + friend
```

---

# Indexing
* Quick Example
```python
greet_a_friend[0]
greet_a_friend[1]
greet_a_friend[len(greet_a_friend)-1]
```

* A string is sequence of characters, we can inspect the object in different ways such as printing the value of each character. 
* The sequence in Python starts with index 0 (zero) and ends with an index of length of the string minus 1.

---

# Defining a string:
* We can define strings in three different ways.
* \#1: Use double quotes 
    * "Hello", "World"
* \#2: Using single quotes 
    * 'Hello', 'World'
* \#3: Using triple single quotes 
    * ('''Hello, world''') 
* \#4: Using triple double quotes 
    * ("""Hello, World""")

---

# String Operations
- Access a character of a string by index
- Indexing can be a positive number
- Indexing can also be negative number
    ```python
        * greeting = "Hello"
        * greeting[0] # returns a new string "H"
        * greeting[len(greeting) - 1] # returns a new string "o"
        * greeting[-2] # returns a new string "l" (second character from the last)
    ```
- Concatenation (+)
- Repetition (*)
- upper()
- lower()

---

# String Operations (Cntd)

- len(str) - works on any sequences
- Slicing
   - string[start-index, end-index, step]
- String formatter
    ```python
        "{}{}{}{}".format(1, 2, 3, 4)
    ```
- Formatted String
    ```python
        f"{1}{2}{3}{4}"
    ```
- Unicode Strings
- Pattern Matching

---

# Exercises

1. Define a variable named "greeting" and assign "Hello" to it. Print the variable greeting using print function.

2. Define two variables "greeting" and "name". Assign a greeting to the variable and your friend's name to the variable name. Concatenate two strings with a space in between and print the resultant string.

3. Assign the following string to a variable (name the variable meaningfully) and print them.
   - print a inspirational quote
   - print a text that has single quote in it (Ex: variable's value)
   - print a text that has double quote in it (Ex: "Hello")
   - print a poem (multiple line string)

4. Write a program to print the length of a string (use the function - len)

---

# Exercises (Cntd)

5. Assign the string "Python is easy to learn" and print the following.
    - substring by slicing
    - print the string "Python"
    - print the string "easy"
    - print the string "learn"
    - print the last character in the above string
    - convert the above string to lower case
    - convert the above string to upper case
    - count the number of "t", "a", "Python" in the above string
    - print the starting index of the substring "Python", "easy" using string's find method
    - Replace "easy" with "super easy" and print the resultant string. Use string's replace method

6. Using string formatter, print the following greetings for several of your friends ({}, {}, How are you doing?)
    - "Hi, Ram, How are you doing?"
    - "Hi, Krishna, How are you doing?"
    - "Hello, Ganesh, How are you doing?"

---

# Exercises (Cntd)


7. Repeat the above exercise using format string (works only in Python 3.6 or above)

8. Write a program to split the following string as independent strings.
    - "India-is-a-great-country"

9.  Write a program to convert the following string "India-is-a-great-country" to "India is a great country"

10. Write a program to count number of times each character is present in the given string.

11. Write a program to count number of special characters present in the given string.

12. Write a program to do the following.
    - Convert string "2" to integer 2
    - Convert string "2.0" to float 2.0

---

# Exercises (Cntd)

13. Write a program that takes a list of strings and return the length of the longest string.

14. Write a program that takes a date in MM-DD-YYYY format and returns in YYYY-MM-DD format

15. Write a program to find number of times the vowels - "a", "e", "i", "o" and "u" is present in a string.

16. Write a program to remove white spaces from beginning and end of a string.

17. Write a program to sort a list of strings based on the length of the strings

18. Write a program to find ASCII value of given character

19. Given a string, write a program to return list of corresponding ASCII characters. If the string is "hello", you should return a list that has ASCII values of each character in corresponding index in list

---

# Exercises (Cntd)


20. Write a program to remove the leading whitespaces in a string

21. Write a program to remove the trailing whitespaces in a string

22. Write a program to remove both leading and trailing whitespaces in a string

23. Given an arbitary string, write a program to find out number of alphanumeric characters

<!---
\# Exercises on String Slicing
TO BE FILLED
--->
