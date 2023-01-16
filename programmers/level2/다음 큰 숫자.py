def to_binary_and_count(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2

    return count


def solution(n):
    cnt = to_binary_and_count(n)
    s = n + 1
    while True:
        if to_binary_and_count(s) == cnt:
            break
        s += 1
    return s


if __name__ == "__main__":
    n = 15
    print(solution(n))
