"""
Question:
Write a program to check how a given number can be expressed
as the sum of two prime numbers.

Input:
A single integer number.

Output:
Print all possible pairs of prime numbers whose sum equals
the given number.

Example:
Input: 34
Output:
3 + 31 = 34
5 + 29 = 34
11 + 23 = 34
17 + 17 = 34
23 + 11 = 34
29 + 5 = 34
31 + 3 = 34
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primeadd(num):
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            print(i, "+", num - i, "=", num)


# Sample Input
primeadd(34)
