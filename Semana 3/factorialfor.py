def factorial (n):
    result = 1
    for i in range(1,n):
        result = result * n
        return result

print(factorial(4))