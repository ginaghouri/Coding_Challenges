def fib(n):
    if n < 2:
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(4))

# fib(4)

# fib(3) + fib(2)

# fib(n)


# fib(2) + fib(1) + fib(1)+ fib(0)

# fib(1) + fib(0) + 1 + 1 + 0

# 1 + 0 + 1 + 1 + 0

# 3
