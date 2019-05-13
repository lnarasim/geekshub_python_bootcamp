layout: true
class: center, middle, inverse

---

# venv
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Python Packages - Revisit
* Python is modular
* Lots of third party libraries
* Excellent support for packages
* Nicer package management through pip
* But

---

# Conflicting Dependencies
* Package management can be complicated
    * When you have conflicting requirements
* Different versions of packages for different projects
    * but you need to develop in same laptop
* You need to run different applications in same server
* Package dependencies can become messy if you work in three different projects
* You want nicer and isolated environment
* VirtualEnv is your solution

---

# Where packages are stored - quick peek
* sys.prefix
* site.getsitepackages()

---

# Virtual Environments (venv)
* Create Isolated envs for Python projects
* Each has its own dependencies
* No limit to the number of virtual environments
* __python -m venv [path where virtualenv to be created]__

---

# venv - directory structure
* Scripts or bin
* include
* lib
* activate/activate.bat - to activate the virtual env
* deactive/deactivate.bat - to deactivate the virutal env

---

# Virtual Env Wrapper
* Manage multiple venvs with single tool
* workon
* deactivate
* mkvirtualenv
* cdvirtualenv
* rmvirtualenv

---

# Exercises

WIP

---

layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---