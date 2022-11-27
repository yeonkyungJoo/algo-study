from collections import deque


def solution(k, tangerine):
    answer = 0

    count = dict()
    for n in tangerine:
        if n not in count:
            count[n] = 0
        count[n] += 1
    result = list(count.items())
    result.sort(key=lambda x: -x[1])
    result = deque(result)
    while k > 0:
        m, n = result.popleft()
        if k >= n:
            k -= n
        else:
            k = 0
            n -= k
        answer += 1

    return answer
