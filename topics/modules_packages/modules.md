layout: true
class: center, middle, inverse

---

# Modules
with [examples](modules.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Modules
* Modules are objects of type "ModuleType"
* Modules have namespaces
* Usually loaded from file
* Modules have execution environment

---

# Import and Namespaces
* Modules can be imported
* Modules are loaded in System Cache
* References gets added
* locals() and globals()
* Attributes can be added to module's namespace
* Examples
    ```python
    import math
    print(math.__name__)
    print(id(math))
    print(math.__dict__)
    print(sys.modules)
    ``` 
---

# Importing
* Checks sys.modules
* Creates a new module type
* Loads source code from the file (if not found in sys.modules cache)
* Add entries to the cache
* Compiles and executes the source code

---

# Exercises


---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---
