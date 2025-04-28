def fib(n: int):
    """
    reucrsive function to find nth fibonacci number
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)
    
    
    
num = 7
ans =  fib(num)
print(ans)