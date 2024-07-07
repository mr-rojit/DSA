def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


def fib(n):
    """
    return nth number of fibonacci series
    0	1	1	2	3	5	8	
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)


print(fib(7))