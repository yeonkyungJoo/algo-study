def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    ch = [0 for _ in range(n + 1)]
    ch[1] = 1
    ch[2] = 2

    for i in range(3, n + 1):
        ch[i] = ch[i - 2] + ch[i - 1]
    return ch[n] % 1234567