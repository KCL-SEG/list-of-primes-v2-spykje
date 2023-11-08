"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
            raise ValueError
    else:
        i = 2
        while len(list) < number_of_primes:
            factor_count = 0
            for j in range(1, 1 + math.floor(math.sqrt(i))):
                if i % j == 0:
                    factor_count += 1
                if factor_count > 1:
                    break
            if factor_count == 1:
                list.append(i)
            i += 1
    return list