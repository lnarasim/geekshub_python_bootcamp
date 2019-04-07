# Python Coding Problems For Practice

1. Install Python in your machine and query the version of the Python installed. Prefer to use Linux over windows. If you do not have Linux, use VirtualBox or Vmware player to install Linux

2. Print the strings - "Hello, World", "Python is a wonderful language", "I am a beginner in Python"

3. Assign the strings in the previous exercise to a variable and use the variable to print the string

4. Get the name of the user as input and greet the user saying "Hi <firstname>"

5. Get the name of the user as inputs and greet the user saying "Good Morning, <firstname>" or "Good Afternoon, <firstname>" depending upon the time of the day

6. Given the radius of the circle, write a program to print the circumference and area of the circle. Write functions to calculate area and circumference

7. Given the area of the circle, write a program to print the radius

8. Given a number, find whether or not it is prime

9. Given a number, find the next prime number (if 8 is the input, the function should return 11. If 11 is input, it should return 13)

10. Given a number, find the prime number that comes first when we count backward. (if 11 is input, it should return 7. If 9 is inputs, it should return 7)

11. Print the command line arguments of the program with each argument printed in a line. Print an error when there are no arguments are given in the command line

12. Write a program to whether or not the given string is a valid email address

13. Given a few words, convert them to lowercase, UPPERCASE, and CamelCase. Print them to the console

14. Given a string, find the length of the string and print it to the console

15. Write a python function that returns first "N" Fibonacci numbers for a given "N"

16. Write a program to find whether the given string is a palindrome or not

17. Write a program that returns GCD of two numbers

18. Write a program that returns LCM of two numbers

19. Create a calculator covering all operations - addition, subtraction, multiplication, division, keeping up to 10 numbers in memory (M+), removing the entries in memory (M-) and clearing all the entries in the memory (AC)

20. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included)

21. Write a program in Python that takes a list and returns two lists - odd and even lists such that the odd list contains a list of all odd numbers even lists contains a list of all even numbers

22. Write a program to sort a list in ascending order

23. Write a program to sort a list in descending order

24. Write a program to find the number of unique numbers in the list

25. For a list that has numbers, find the sum of odd numbers and the sum of even numbers

26. A list has numbers. Write a program to move odd number to start of the list and even number to the end of the list. For example, the list [1,2,3,4,5,6,7,8,9,10] should be transformed to [1,3,5,7,9,2,4,6,8,10]

27. Write a program to find the largest number in the list.

28. Given a number "N" and a list that has numbers, write a program to find the Nth largest element in the list

29. Write a program to find the factorial of the given number

30. Given the value of m and n, write a program find permutation and combination

31. Given a date, write a program to find the number of days between the given date and today

32. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

33. Implement a function that takes as input three variables, and returns the largest of the three.

34. Given a URL, write a program to parse and get the following from the URL
    - The protocol
    - Hostname
    - Port number
    - URL path

35. Write a program to validate IPV4 address

36. Write a program to validate UDP/TCP port numbers

37. Write a program to sort list of numbers without using built-in functions

38. Write a program to count the number of sentences, words and characters in a give page of text

39. Given a list of process ids, write a program to kill all those processes. The program should output successful and errors (if it is not able to kill certain processes)

40. Write a program to convert the output of "netstat -su" command to JSON format (Note: netstat is a Linux command)

41. Write a program to convert the output of the command
    "ifconfig -a" to JSON format

42. Install the tool apache benchmark, write a program that measures the performance of the web server/web service and convert the output of the tool to JSON format. The task is to run the tool from Python, get the output of the tool and convert the output to JSON format

43. You are running a tea shop, write a program to sell the beverages such as "tea", "coffee", "milk" etc. Print the menu card to the user and also total sales of the day for each item and overall sales

44. Given the amount, write a program to find out the minimum number of coins/notes required to total up to the amount. For instance, denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    - For 2000, it should return 1
    - For 2001, it should return 2
    - For 510, it should return 2
    - For 512, it should return 3

45. Write to program to read a text file and return number of sentences, words and characters in the file

46. Write a program in Python that collects the birthdays of your friends that does the following.
    - Given a friend's name, it should return her/his birthday
    - Given a day and month, it should return list of folks whose birthday falls on that day
    - From current day, it should return whose birthday falls next

47. Write a simple password generator tool

48. Write a program in Python that reverses the words in a sentence

49. Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

50. Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list, using a function

51. Read Caesar Encryption (https://en.wikipedia.org/wiki/Caesar_cipher), implement it in Python. You need to write two functions that encrypts and decrypts the messages.

52. Implement the data structure "Stack" using list in Python. The stack should hold 'N' elements, it should perform "push" to add an element to the list and 'pop' to retrieve the last inserted element. Test overflow and underflow scenarios

53. Implement the data structure "Queue" using list in Python. The stack should hold 'N' elements, it should perform "enqueue" to add an element to the list and 'dequeue' to retrieve the oldest inserted element. Test overflow and underflow conditions

54. Store a list of quotes by famous personality, write a program that prints a random quote

55. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
    - D 100
    - W 200
    
    D means deposit while W means withdrawal. Suppose the following input is supplied to the program:
    - D 300
    - D 300
    - W 200
    - D 100
    
    Then, the output should be: 500

56. Ask the user for a string and print out whether this string is a palindrome

57. Write a program that prints the number of times the words are found. For example, "Betty bought some butter, the butter was bitter, so Betty bought some better butter to make the bitter butter, a better butter". You need to print number of times each word is repeated.

58. Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates

59. Install "ETCD" in your Linux VM. Write a simple program to store contact list in ETCD. Read about ETCD from the link - https://coreos.com/etcd/ (for now, implement as single node and later we can do cluster mode)

60. Given a set of three numbers (a, b and c), write a function in Python to find they form Pythagorean Triple. Return True if they are, False if they are not

61. Given a number, find out whether or not it is an Armstrong Numbers

62. Convert the output of the command "df -k" into JSON

63. Write a program to copy the contents of one file to another file getting filenames as inputs through command line. For example,
      - python copy.py source_file.txt destination_file.txt

64. Given a list of numbers in a list, write a program to find out mean, mode and median

65. Write two functions in Python one to convert Farenheit to Celcius and Celcius to Farenheit

66. Given a webpage (URL), extract all the links and find out whether or not those links are dead links (dead links are the links that do not fetch any content when clicked)

# GREAT JOB

* COMMIT ALL THE CODE THAT YOU HAVE DONE TO GITHUB. CREATE YOUR OWN REPOSITORY AND FEEL HAPPY THAT YOU HAVE REACHED THIS FAR.

* YOU HAVE DONE AN AMAZING JOB OF PROGRESSING AND WITH LITTLE MORE FOCUS YOU CAN DO WONDERS WITH PYTHON. BY NOW, YOU WOULD HAVE UNDERSTOOD HARD WORK PAYS OFF AND NOW YOU ARE READY TO LEVEL-UP TO TAKE PYTHON LITTLE MORE SERIOUSLY GROWING YOU CAPABILITY TO WRITE PRODUCTION READY CODE. A LITTLE WHILE FROM NOW, YOU WILL HAVE YOUR DREAM JOB AND WRITING SOFTWARE THAT IS USED BY SOMEONE. KEEP UP THE GREAT WORK

* CREATE A VIRTUAL ENVIRONMENT AND RUN THESE EXERCISES RESOLVING ALL DEPENDENCIES

* NOW THAT YOU HAVE BECOME A ROCK STAR CODER, CAN YOU WRITE AUTOMATED TESTS USING "PyTest"? THIS WILL MAKE YOU A COMPLETE DEVELOPER (A DEVELOPER WHO KNOWS HOW TO WRITE TESTS, HOW TO AUTOMATE THEM)

* REGISTER WITH HACKERRANK AND START SOLVING PROBLEMS AND EARN BADGES. MOST COMPANIES ARE PLANNING TO USE HACKERRANK OR SIMILAR PORTAL FOR JOB ASSESSMENT OR USING SIMILAR QUESTIONS IN INTERVIEWS. HACKERRANK PROBLEMS ARE TOUGHER TO SOLVE AND GIVES SENSE OF ACCOMPLISHMENT TOO.

# Go head and develop some mini-projects, ALL THE BEST

## Check the tools problems and try to do few of the tools. Pick up some simple straight forward tools and a couple of tough tools
