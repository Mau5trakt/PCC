def factorial (n):
    result = 1
    for n in range (1, n+1):
        result = result * n
                                #'''
                                #i put the 'n + 1' expresion bc in the programation the
                                #computer starts from 0 and if i put 4 in the function
                                #what the computer really does is (0,1,2,3).
                                #'''
    return result


print(factorial(4)) # should return 24
print(factorial(5)) # should return 120