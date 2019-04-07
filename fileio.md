layout: true
class: center, middle, inverse

---

# File I/O
with [examples](examples/fileio.ipynb)
## [GeeksHub](http://www.geekshub.in)
### [info@geekshub.in](mailto:info@geekshub.in)

---

name: inverse
layout: false

# Files
* Files (objects) interface with file system files
* Create file using "open" function
* Depending upon the mode, some/all of the methods can be invoked
```python
    file_obj = open("filename", "mode")
```

---

# File Modes
* 'r' - open for reading (default)
* 'w' - open for writing, truncating the file first
* 'x' - create a new file and open it for writing
* 'a' - open for writing, appending to the end of the file if it exists
* 'b' - binary mode
* 't' - text mode (default)
* '+' - open a disk file for updating (reading and writing)

---

# Typical Flow
* Open a file
* Perform the operation
* __Close the file__
```python
    file_object = open("test.txt","r")
    contents = file_object.read()
    print(contents)
    # after using the file, you need to close it
    file_object.close()
```
---

# Preferred Way
```python
with open('what_are_context_managers.txt', 'r') as infile:
    for line in infile:
        print('> {}'.format(line))
```

---

# Reading a file
* read(size) - reads size characters or all characters if size is not given
```python
contents = file_object.read()
```

* readline() - reads a line for every call
```python
contents = file_object.readline()
```

* readlines() - reads all the lines
```python
file_object = open("test.txt", "r")
for line in file_object.readlines():
    print(line)
file_object.close()
```

* reading by using file object
```python
file_object = open("test.txt", "r")
for line in file_object:
    print(line, end="")
file_object.close()
```

---

# Writing to a file
* write()
* writeline()

# seek - moving file pointer
* Move file pointer to a position to perform any specific operation from that position
```python
seek(offset, whence)
```
---

# Other methods
* fileno
* flush
* readable
* seekable
* truncate
* tell
* writable
* closed
* name

---

# Let us see some (more) examples
# Try as you see it

---

layout: true
class: center, middle, inverse

---

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)