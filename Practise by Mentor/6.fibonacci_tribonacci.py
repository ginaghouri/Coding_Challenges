def fib(n):
    if n < 2:
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(4))

def trib(n):
    if n < 2:
        return n
    if n == 2:
        return 1
        
    return trib(n-1)+trib(n-2)+trib(n-3)

print(trib(9))

# fib(4) https://stemettes.org/zine/articles/fibonacci-in-nature/

# fib(3) + fib(2)

# fib(n)


# fib(2) + fib(1) + fib(1)+ fib(0)

# fib(1) + fib(0) + 1 + 1 + 0

# 1 + 0 + 1 + 1 + 0

# 3
