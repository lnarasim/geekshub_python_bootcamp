layout: true
class: center, middle, inverse

---

# Exceptions
with [examples](examples/exceptions.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Errors
* Errors are parsing errors introduced due to bad syntax
  * Missing a mandatory token
    * Ex: colon (:) at the end of for/while loop
  * Python Interpreter displays approx position
    * Filename, line number and a ^ symbol

---

# Exceptions
* Exceptions are program logic error
* Syntax is correct
* Python cannot fix logic error
* Left to developers to fix (handle) logic error
    * What should the program do if the file is not there
    * What should the program do if the remote server is not responding

---

# Handling Exceptional Situation
* Handle exceptional situation by raising exception
* Handle exceptions by recovering the function and possibly take the application towards good
    * Do not mask failure. When the program fails, it should cry
* Use exceptions provided by Python
* User (developer) defined exceptions

---

# Exceptions in Nutshell
```python
try:
    # some statements go here that you suspect might lead to some exceptions
    pass

except ValueError:
    # handle value error
    pass
except IOError:
    # handle IO error
    pass
except (RuntimeError, TypeError):
    # handle two errors in one go, but understand why you should be doing this
    pass
except:
    # Handle all other exceptions. Again should be used with great care

else:
    # What should i do if there is no exception
    pass

finally:
    # Run this code, no matter what.
```

---

# Handle (catch) Exceptions - Simple Case
* Use try..except..else..finally blocks
```python
    try:
        a = 0
        b = 1
        c = b/a
    except ZeroDivisionError as exp:
        print(exp)
        print(exp.args)
        print(type(exp))
        print(issubclass(ZeroDivisionError, Exception))
```
---

# Handle Exceptions - Much cleaner way
```python
    try:
        a = 1
        b = 1
        c = b/a
        d = a + 1
    except ZeroDivisionError as exp:
        print(exp)
        print(exp.args)
        print(type(exp))
        print(issubclass(ZeroDivisionError, Exception))
        print("Zero division error")
    except TypeError as type_exp:
        print(type_exp)
        print(type_exp.args)
        print(type(type_exp))
        print(issubclass(TypeError, Exception))
        print("Type error")
    else:
        print("no exception occured, good job")
    finally:
        print("This block runs no matter what")
```

---

# Raising Exception
* "raise" keyword to raise exceptions
```python
    def divide(dividend, divisor):
    if divisor == 0:
        exp_str = "Exception while doing {0}/{1}".format(dividend, divisor)
        raise ZeroDivisionError(exp_str)
    return dividend/divisor

    print(divide(1, 1))
    print(divide(1, 0))
```

---

# Extending Exception
* Create your own exception by extending Exception class
    ```python
    class ArithmeticException(Exception):

        def __int__(self, number):
            self.number = number

    def divide(dividend, divisor):
        if divisor == 0:
            raise ArithmeticException(divisor)
        return dividend/divisor

    print(divide(1, 1))
    print(divide(1, 0))
    ```
# Special Case - while/for loops with break
* finally is always executed
* Even when control goes out of try block (break, continue or return)