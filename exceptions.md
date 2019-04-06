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
