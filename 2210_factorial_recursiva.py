# if n is a positive integer, n! = n(n-1)(n-2)...(3)(2)(1). The product of all positive integers less than or equal to n
# 0! = 1
def factorial(n):
    if n < 0:
        return('{} is not a positive integer '.format(n))
    elif n >= 1:
        return(n * factorial(n-1))
    else:
        return(1)

print(factorial(4))
print(4*3*2*1)
print(factorial(0))
print(factorial(-1))
