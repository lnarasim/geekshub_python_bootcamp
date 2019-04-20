layout: true
class: center, middle, inverse

---

# Packages
with [examples](packages.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Packages
* Packages are modules
* They contain modules and packages
* If a module is a package, it should have \_\_path\_\_
* Modules and packages do not have to be entities in the file system
* Packages represent a hierarchy of modules/packages
    * Helps organize code and ease of use
* Examples:
    * pack1.mod1
    * pack1.pack1_1.mod1_1
    * Found in \_\_path\_\_

---

# Importing Nested Packages
* import pack1.pack1_1.module1
    * imports pack1
    * imports pack1_1
    * imports module1
* sys.modules has pack1, pack1_1 and module1
* Namespace where the import was run contains pack1

---

# File Based Packages
* Package paths are created using file system directories and files
* Packages use directories
* Modules are files
* \_\_init\_\_.py tells Python that directory is a package
* \_\_init\_\_.py has package code
* Ex:
    * app/
        * pack1/
            * \_\_init\_\_.py
            * module1.py
            * module2.py
* import pack1 - imports \_\_init\_\_.py as module pack1

---

# Packages and Modules - dunder variables
* module1.\_\_file\_\_
* module1.\_\_package\_\_
* module1.\_\_path\_\_ (throws error as modules do not have \_\_path\_\_)
* pack1.\_\_file\_\_
* pack1.\_\_package\_\_
* pack1.\_\_path\_\_

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
