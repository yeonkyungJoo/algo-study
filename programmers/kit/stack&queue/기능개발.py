from collections import deque
def solution(progresses, speeds):

    days = deque()
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]

        rest = 100 - progress
        day = (rest // speed) if rest % speed == 0 else (rest // speed) + 1
        days.append(day)

    answer = []
    stack = []
    count = 0
    while days:
        d = days.popleft()
        if not stack:
            stack.append(d)
            count = 1
        else:
            if stack[-1] >= d:
                count += 1
            else:
                answer.append(count)
                stack.append(d)
                count = 1
    answer.append(count)
    return answer

if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))