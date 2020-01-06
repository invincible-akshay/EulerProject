import sys
sys.path.append('../')
from libs import test_framework as t_fwork

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_sum_3_5_mults_till_n(n):
    i = 3
    res = 0
    while i < n:
        if i % 3 == 0:
            res += i
            if i % 5 == 0:
                i += 3
            else:
                i += 1
        elif i % 5 == 0:
            res += i
            i += 1
        else:
            i += 1
    return res


print('** Running Tests now **')
tests = t_fwork.CustomTests()
tests.run_test(get_sum_3_5_mults_till_n, 23, 10)
tests.run_test(get_sum_3_5_mults_till_n, 195, 30)
tests.run_test(get_sum_3_5_mults_till_n, 200, 30)
