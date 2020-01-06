import math
import sys
from libs import test_framework as t_fwork
sys.path.append('../')

"""
@UTHOR: AKSHAY NEHE
Q. The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    # print('Checking n = {0}'.format(n))
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        largest_val = int(math.floor(math.sqrt(n)))
        i = 2
        while i <= largest_val:
            # print('n is: {0} and i is {1}'.format(n, i))
            if n % i == 0:
                return False
            i += 1
        return True


def get_largest_prime_factor(n):
    i = 2
    largest_prime = None
    largest_val = int(math.floor(math.sqrt(n)))
    print('largest val is: {0}'.format(largest_val))
    while i <= largest_val:
        if n % i == 0:
            if is_prime(int(n/i)) is True:
                return int(n/i)
            elif is_prime(i):
                largest_prime = i
        i += 1
    return largest_prime


tests = t_fwork.CustomTests()
# 1 1 2 3 5
tests.run_test(get_largest_prime_factor, 5, 30)
tests.run_test(get_largest_prime_factor, 5, 40)
tests.run_test(get_largest_prime_factor, 11, 99)
tests.run_test(get_largest_prime_factor, 29, 13195)

print('Largest prime factor of 600851475143 is: {0}'.format(get_largest_prime_factor(600851475143)))
