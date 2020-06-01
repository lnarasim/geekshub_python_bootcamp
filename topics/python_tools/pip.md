layout: true
class: center, middle, inverse

---

# pip
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# PIP
* Standard package manager for Python
* Install and manages the packages (apart from what is available in standard library)
* PIP comes by default in Python during Python installation
* Python Package Index - https://pypi.org
    * Contains all frameworks, tools and libraries that can be installed using pip command
    * Repositiory of packages
    * Extensive set of packages
    * Developed by community

---

# pip - basic scenarios
* help - documentation about the command
* search- Search specific packages in PyPi
* show - displays information about the packages
* list - list of packages installed
* install - installs/upgrades package with dependencies
* uninstall - removes the packages
* upgrade - upgrade packages
* download - downloads the packages
* freeze - list of packages installed in requirements format
* check - Verify installed packages have compatible dependencies

---

# pip - examples
* pip search pytorch
* pip list
* pip list -o (--outdated)
* pip install requests
* python -m pip install --upgrade pip
* pip show requests
* pip freeze > requirements.txt
* pip install -r requirements.txt (>= and <= can be used in requirements.txt)
* pip install --upgrade -r requirements.txt
* pip search requests
* pip uninstall requests
* pip uninstall requests -y
* pip uninstall requests -r requirements.txt - y

---

# Exercises

1. Install "requests" using pip

2. Upgrade a package that is already installed in the system

3. Display all the installed packages

4. Display all the installed packages in requirements format

5. Install packages through requirements.txt

6. Unstall a package

7. Show information about a package.

---

# Exercises (cntd)

8. Identify the list of dependencies for "requests" package

9. Use import to verify whether the packages are installed properly

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---