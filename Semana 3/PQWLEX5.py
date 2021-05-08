import math


def sum_divisors(n):
    sum = 1
    # Return the sum of all divisors of n, not including n
    div = 2
    if n == 0:
        return 0

    while div < n / 2 + 1:
        if n % div == 0:
            sum += div
        div += 1

    return sum


print(sum_divisors(6))  # Should be 6 (sum of 1+2+3)
print(sum_divisors(12))  # Should be 16 (sum of 1+2+3+4+6)
