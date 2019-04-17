layout: true
class: center, middle, inverse

---

# File I/O
with [examples](fileio.ipynb)
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

# Open a File
- How to open a file
```python
    file = open("filename", "mode")
```
- "filename" is straightforward. It can be either relative path or absolute path
- "mode" is explained below

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

# File Modes/Access Flags - Little Detail
* Read (r)
    - default if not specified
    - can only read
    - File index/pointer points to first character (seek 0)
* Write (w)
    - can only write
    - cannot read
    - Truncates the file
    - File index/pointer points to first character (seek 0)
* Create and Write (x)
    - Create the file
    - Writable
    - Cannot read

---
# File Modes/Access Flags - Little Detail (Cntd)
* Append (a)
    - Create a file if the file does not exist
    - Open the file for appending. The file pointer points to end of the file
    - Can only Write
    - Cannot read
* Open a disk file for updating (+)
    - Goes along with any of the modes - read, write, create, append
    - File index/pointer points to first character (seek 0)
* Binary mode (b)
    - Anything beyond text files
* Text mode (t)
    - default if not specified
    - applicable for text files that are in human readable form

---

# Close the file
- Need to close explicitly to release system resources
- Writes buffer to the file storage on close
- Very important but often forgotten

---

# Reading a file
- Always reads from the current file pointer location
- file.read(size)
- file.readline()
    - reads a line, moves line by line
    - system resources not wasted as reading happens on need basis and when required
    - reading file object like this
        ```python
            file_obj = open("1.txt", "r")
            for line in file_obj:
                print(line)
        ```
- file.readlines()
    - reads all the lines in the file
    - creates a list
    - not memory efficient if you are not going to use all the lines.

---

# Writing to a file
- Always writes from the current file pointer location
- file.write(data)
- file.writeline()
- returns the number of bytes written

---

# Seek or moving file pointer
- Moves file pointer to specific offset
```python
    seek(self, offset, whence=0, /)
```
- offset from whence
- offset can be negative
- whence is position
    - 0 is starting of the file
    - 1 is current file pointer position
    - 2 is end of the file

---

# Context Manager
- use "with" to open a file
- file automatically closes after it exits out of the context
- can still inspect file object
- cannot perform any operations on the file as the file is already closed immediately after the context block
- Helps to avoid leaks of descriptor
- Cleaner way to work on files

---


# Context Manager - Example

```python
with open('what_are_context_managers.txt', 'r') as infile:
    for line in infile:
        print('> {}'.format(line))
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

# Exercises

1. Open a file in read mode and print the contents of the file line by line

2. Open a file in read mode and print the contents of the file in one go

3. Open a big file, say with a size of 20MB and try to print the contents

4. Write a tool that prints the list of files in a given directory with the size of each file. Use command line arguments to get the target directory from the user.

5. Write a tool that takes a filename as input and compresses it (may be zipping or archiving it using zip, tar etc). Use at least two methods of compression

6. Write a program to calcuate checksum of given file.

7. Take a text file. Assume that it is 2-D matrix with m * n. Write a program that transpose the contents of the file (rows should be converted to colmuns and columns should be converted to rows)

---

# Exercises (Cntd)

8. Write a file split tool. If you have a huge file, split the file into smaller chunks of 1MB and save the chunks as separate files ending with .1, .2, .3, .4 etc. For examples the file "5MB.txt" should be split into five files - "5MB.txt.1", "5MB.txt.2", "5MB.txt.3", "5MB.txt.4" and "5MB.txt.5"

9. Document various errors you encountered while doing these exercises. Explain each error and how did you fix those errors. How will you prevent it from happening

10. Write a program that reads a file in chucks and stores in another file.

11. Write a program that builds a dictionary of words in a file and number of times each word present in the file. The word should be case insensitive (Python is same as python or any other forms)

12. Write a program that stores the contents of a dictionary in a file and constructs back the dictionary from the file. You have to implement two functions - serialize that converts dictinoary to file and deserialize that converts the contents of a file to a dictionary in Python

---

# Exercises (Cntd)

13. Implement a simple translation software of different languages with following features
    - The words of all words are stored in single file (say words.txt)
    - Input #: word
    - Input #2: Language of input #1
    - Input #3: Language to be translated
    - Output: Displays the translated word

14. Implement Unix command - "head". The command lists first "n" lines of a file. If the number is not specified, it displays first 10 lines

15. Implement Unix command - "tail". The command lists last "n" lines of a file. If the number is not specified, it displays last 10 lines

16. Write a program to find the longest line in a file and number of characters in it

17. You know how to print a character using print function. Can you print some characters using file sys.stdout. Observe what is happening.

---

# Exercises (Cntd)

18. Write a simple anti-virus software. The program has a set of signatures that matches various viruses and flags if there is a match in target files. All the signatures of viruses are stored in a specific directory. The input to the program should be "signature directory" and "target directory" and the output should be a report of the scanning.

19. Generate HTML report for the anti-virus software

20. Write the remediation logic for the anti-virus software. The remediation can be the following.
    - Moving the affected file to a quarantine (a separate directory)
    - Deleting the infected file
    - Disabling the network connection so that the virus does not spread to other system

21. Read the following post about structure of .pyc file. Write a program that reads a .pyc file and returns whether it is a valid .pyc file or not. [Targeting The Python Virtual Machine I: The Internal Structure of .pyc Files](http://blog.braulio.me/2018/06/28/internal-structure-pyc-files.html)

---

# Backup

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
layout: true
class: center, middle, inverse

# Thank you :-)

# [GeeksHub](http://www.geekshub.in)
_**Co-Creating Tomorrow **_
### [info@geekshub.in](mailto:info@geekshub.in)

---
