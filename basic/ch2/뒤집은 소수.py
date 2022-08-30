import sys
import math

#sys.stdin = open("input.txt", "rt")


def reverse(x):
    tmp = []
    while x > 0:
        tmp.append(x % 10)
        x //= 10
    return int(''.join(map(str, tmp)))


def isPrime(x):

    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    rev = reverse(num)
    if isPrime(rev):
        print(rev, end=' ')
