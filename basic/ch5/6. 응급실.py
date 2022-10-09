from collections import deque
if __name__ == "__main__":
    N, M = map(int, input().split())
    patients = list(map(int, input().split()))

    queue = deque([(idx, h) for idx, h in enumerate(patients)])
    _max = deque(sorted(patients, reverse=True))
    cnt = 0
    while queue:
        i, h = queue.popleft()
        if h == _max[0]:
            _max.popleft()
            cnt += 1
            if i == M:
                print(cnt)
                break
        else:
            queue.append((i, h))
