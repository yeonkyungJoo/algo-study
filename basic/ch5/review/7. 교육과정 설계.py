from collections import deque
if __name__ == "__main__":
    need = input()
    N = int(input())

    for idx in range(N):
        queue = deque(input())
        result = True
        _need = deque(need)
        while queue:
            c = queue.popleft()
            if c in _need:
                if c == _need[0]:
                    _need.popleft()
                else:
                    result = False
        if _need:
            result = False
        print("#{} {}".format(idx+1, 'YES' if result else 'NO'))