layout: true
class: center, middle, inverse

---

# Dictionary
with [examples](examples/dictionary.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Composite Datatype

* Integer, float, character, boolean are primitive types. 
* We store some value in these primitive types. 
    * For example, the number of stars in our galaxy, the temperature of Chennai and do you want to learn Python.
    * The number of students in a class can be expressed as integers. But the number of students in each class cannot be expressed as integers. 
* We need some form of group. We have seen in lists that it helps us store group of items and reference each item by index, iterate the list and perform basic operations such as adding an element, updating the object, deleting the object, inspecting the list for specific object and so on.

---

# Dictionary
* Dictionary is another form of data structure that helps us store and retrieve objects. 
* Stores as key, value pair
* Key is the index and the value what is stored in the index
* The dictionary uses "any immutable/hashable" object as key and any object as its value. 
* It works pretty much like an associative array.

---

# Key properties
- Dynamic, grows/shrinks in size (like list)
- Since it is Dynamic, it is mutable (like list)
- It stores values as key - value pairs. The key should be hashable/immutable (unlike list)
- Ordered in the order the keys were inserted

---

# Creating Dictionary

* Creating a dictionary - Method #1:
```python
        detail = {'name' : 'lakshmi', 'age': 18, 'id' : '007'}
```

* Creating a dictionary - Method #2:
```python
        another_dictionary = {}
        another_dictionary['name'] = 'Lakshmi'
        another_dictionary['age'] = 18
        another_dictionary['id'] = '001'
```

* Creating a dictionary - Method #3: By sequences
```python
        tuple_dict = dict([('name', 'Narayanan'), ('age', 20), ('id', '002')])
```

* Creating a dictionary - Method #4: By keyword arguments
```python
        kw_dict = dict(name='Balaji', age=25, id='100')
```

* Refer help(dict) from Python documentation

---

# Dictionary With Examples

* Create a dictionary that is empty

```python
detail = {}
print(detail)
```

* Another way of creating a dictionary that is empty.

```python
detail = dict()
print(detail)
```

* What does an empty dictionary evaluates to?

```python
if detail:
    print("Dictionary is not empty")
else:
    print("You guessed it right, the dictionary is EMPTY",
            "and that evaluates to boolean 'False'")

print()
```
```python
""" 
You do not create a dictionary for being empty. You want to store values, 
retrieve values, use it for something useful. Generally, we create empty 
data structures when we do not know what to store at the moment of creation 
but we will update/use it as we work on the application logic. This should 
only be the reason why we create empty dictionary. 

If you know what to store while creating the dictionary, you should never 
be creating empty dictionary rather use others forms of instantiation given 
below

"""
```
---
# Dictionary With Examples (Cntd)
* Let us create a dictionary - Method #1
* It is as simple as the following

```python
detail = {'name' : 'lakshmi', 'age': 18, 'id' : '007'}
print(detail)
```

* Let us get the value of name

```python
print(f"Value of 'name' is {detail['name']}")
print(f"Value of 'age' is {detail['age']}")
print(f"Value of 'ID' is {detail['id']}")
```

* Let us update age to 19, yeah today is my birthday

```python
detail['age'] = 19
print(f"Value of 'age' is {detail['age']}")
```

* Let us delete name, age, id and print the dictionary
```python
del detail['name']
del detail['age']
del detail['id']
print(detail)
```

* Let us create a dictionary - Method #2
```python
another_dictionary = {}
another_dictionary['name'] = 'Lakshmi'
another_dictionary['age'] = 18
another_dictionary['id'] = '001'

print(another_dictionary)

```

* Let us create a dictionary - Method #3, by passing a list of tuples/sequences
```python
tuple_dict = dict([('name', 'Narayanan'), ('age', 20), ('id', '002')])
print(tuple_dict)
```

* Let us create a dictionary - Method #4, by passing a keyword arguments
```python
kw_dict = dict(name='Balaji', age=25, id='100')
print(kw_dict)
```

* Let us iterate over all the keys and print them one by one
```python
print("The keys in the dictionary are:")
for key in kw_dict.keys():
    print(key)

print()

print("The values in the dictionary are:")
# Let us iterate over all the values and print them one by one
for value in kw_dict.values():
    print(value)

print()

print("The key-value pairs in the dictionary are:")
# Let us iterate over all the items and print them one by one as key-value pair
for key, value in kw_dict.items():
    print(f"{key} = {value}")

print()
```
* Let us access a key that does not exist
```python
print(f"{kw_dict['does_not_exist']}")
```

* Let us access a key that does not exist but still get away without any error
* To run this statement, you have comment the previous statement
```python
print(f"Value of {'name'} is {kw_dict.get('name')}")
```

* Let us access a key that does not exist
```python
print(f"Value of {'does_not_exist'} is {kw_dict.get('does_not_exist')}")
```

* Let us access a key that does not exist, but passing a string
```python
print(f"Value of {'does_not_exist'} is {kw_dict.get('does_not_exist', 'No Value')}")
```

---
# Dictionary - Operations

* Let us delete a key
```python
del kw_dict['name']
print(kw_dict)
```

* Update a dictionary
```python
kw_dict.update(tuple_dict)
print(kw_dict)
```

* Pop a key from the dictionary
```python
value = kw_dict.pop('name')
print(value)
print(kw_dict)
```

* Pop a key that does not exist
```python
value = kw_dict.pop('does_not_exist')
print(value)
print(kw_dict)
```

* Pop a key that does not exist, but let us pass a default value
```python
value = kw_dict.pop('does_not_exist', None)
print(value)
print(kw_dict)
```

* Let us load the dictionary again
```python
kw_dict.update(tuple_dict)
print(kw_dict)
```

* Let us understand popitem.
```python
value = kw_dict.popitem()
print(value)
print(kw_dict)

kw_dict.update(tuple_dict)
```

* Dictionary - Copy and Clear
```python
new_dict = kw_dict.copy()
print(new_dict)
print(kw_dict)
print(new_dict is kw_dict)

new_dict['name'] = "new name"
print(new_dict)
print(kw_dict)

kw_dict.clear() # what does this do?
print(kw_dict)
kw_dict.update(tuple_dict)

new_dict = kw_dict
print(new_dict)
print(kw_dict)
print(new_dict is kw_dict)

new_dict['name'] = "new name"
print(new_dict)
print(kw_dict)
```
---

# Exercises
1. Define a dictionary for storing contacts lists. Typically, you need to implement to store your friends' list with following details.
    - name as key, value as phone number
    - print the dictionary

2. For the dictionary defined in the previous problem, print all the values by using the key as index. For example: contacts['Ram'], contacts['Krishna']

3. Try printing the value of the key that does not exist and observe the behavior

4. For the dictionary defined in the previous problem, print the following.
    - print all the keys
    - print all the values
    - print key - value pairs

5. Using dictionary's get method, retrieve the following.
    - value of the key that exists
    - value of the key that does not exist
    - value of the key that does not exist but passing a default value to get method

6. Add a contact name and phone to the dictionary.
    - Ex: contacts['Bhushan'] = 9238493893

7. Now, one of your friends has changed his mobile number, write the code snippet to update his phone number.

8. Few of your friends have changed their mobile numbers, write the code to update their numbers in your contacts directory using dictionary's update() method. Observe what happens.

9. Write the code to delete/remove a key using del

10. Write the code to delete/remove a key using dictionary's pop method.

11. What is the difference between deleting keys using del versus pop method?

12. Write a program to find length of a dictionary

13. Loop through the dictionary and print all the keys

14. Loop through the dictionary and print all the values

15. Loop through the dictionary and print all the keys and corresponding values as key - value pairs with each pair printed in a newline

16. What is the type of dictionary? Find it programmatically.

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---