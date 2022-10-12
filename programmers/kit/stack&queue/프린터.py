from collections import deque
def solution(priorities, location):

    _priorities = deque()
    for idx, priority in enumerate(priorities):
        _priorities.append((idx, priority))

    sorted_priorities = deque(sorted(priorities, reverse=True))
    order = 0
    while _priorities:
        idx, priority = _priorities.popleft()
        if priority == sorted_priorities[0]:
            order += 1
            if idx == location:
                return order
            sorted_priorities.popleft()
        else:
            _priorities.append((idx, priority))

    return order + 1

if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))