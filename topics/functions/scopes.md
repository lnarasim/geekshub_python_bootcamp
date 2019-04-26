layout: true
class: center, middle, inverse

---

# Scope
with [examples](scopes.ipynb), [global](local_global_scopes.ipynb), [nonlocal](nonlocal_scope.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Scope
* Scopes are namespaces
* Objects can be accessed using the name in various part of the code
* Name bound to objects exist only in specific parts of the code
* Name to Object bindings are stored in namespaces
* Various scopes
    * Local - function
    * Module or Global
    * Built-in
    * Non Local (enclosing scope, can be any level)

---
# More on Scopes
* Global
    * Module scope
    * Visible only in the file
* Local
    * Defined in a function
    * Created when function is called and deleted when function is returned
    * Every time a function is called, scope is created newly
* built-in
    * Namespaces/scopes made available by default
* Non Local
    * Finds variable in enclosing scope (as functions can be nested)
    * Looks for enclosing local scopes until it first comes across the specific variable name
    * Does not look in global scope
    * Throws error when nonlocal variable not found

---

# Masking
* Local variable masks enclosing/global/built-in scopes 
    * When global/nonlocal is not used, the variable is defined
* Global masks built-in

---

# Scope Resolution
* No keywords (used in RHS assgined to another variable) 
    * Local -> Enclosing Local -> Global -> Built-in
* No keywords (used in LHS) - masks the previous scopes
* global - uses global and built-in
* nonlocal - uses one of the variables in enclosing function but not global
* Variable names once created in scope, never disappears until the scope/namespace is deleted

---

# Exercises

* WIP

---
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---