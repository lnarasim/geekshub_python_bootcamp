## Iterators and Iterables

1. Iterate over a set using for loop and prove that set is unordered

2. Implement your own class that prints the mathematical table. The initializer of the class takes only one parameter which is the table to be printed. Implement a method "get_next_row" that prints numbers 3, 6, 9, 12, 15....,30 for three table object. Note that the maximum number that should be printed is 30 and after that "get_next_row" should not return anything (think of how you can handle it). Use for loop to test whether your code works for at least couple of tables.

3. Test #2 using infinite while loop (while True) and ensure that you break out the loop when you no longer able to iterate

4. Reimplement #2 (and #3) using iterator protocol

5. Implement an iterable of length "n" that generates random numbers between x and y.

6. Implement random number generation to generate "n" rando numbers using iterator protocol

7. Verify how iterator protocol works in conjuction with for loop and list comprehension. Add print statements to all the methods of iterator to understand how it works

8. Given a list of web address, write an iterator and iterable protocol that verifies whether or not the web addresses are up/reachable. The idea is to scan all web address one by one and return the status as and when the web address is encountered. Also add a logic to try two times before giving-up or concluding that the web service is not up.

9. Implement #8 as two different classes - iterable and iterator

10. Implement #9's iterator as nested class (as they are related to one another and coupled)

11. Implement sequence protocol and verify how it works in for loops and list comprehensions

12. Implement an inifite iterator. (ex: prime number generator)

13. Implement a cyclic iterator for a list. A cyclic iterator is an infite iterator that never ends.

14. 