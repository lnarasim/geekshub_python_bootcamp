d = dict()

def fib(n):
    if n < 0:
        raise ValueError("Invalid value")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n in d:
            result =d[n]
        else:
            result = fib(n-1) + fib(n-2)
            d[n] = result
        return result


def is_prime(n):
    if n <= 0:
        raise ValueError("Invalid input")
    if n == 1:
        return False
    if n <= 3:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

