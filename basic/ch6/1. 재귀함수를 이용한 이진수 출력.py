import sys

# sys.stdin = open("../input.txt", "rt")
N = int(input())


def recursive(n, result):
    if n == 0:
        return ''.join(list(reversed(result)))
    return recursive(n // 2, result + str(n % 2))


print(recursive(N, ''))
