# write Fibonacci series up to n

def fib(n):
    """Print a Fibonacci series up to n."""
    a = 0
    b = 1
    
    while a < n:
        print(a, end=' ')
        #a = b
        #b = a + b
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(20000)
