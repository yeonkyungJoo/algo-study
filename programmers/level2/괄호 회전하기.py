from collections import deque


def solution(s):
    answer = 0
    q = deque(s)
    for _ in range(len(s)):
        q.append(q.popleft())
        if q[0] in (')', '}', ']'):
            continue
        if q[-1] in ('(', '{', '['):
            continue

        stack = []
        copied = q.copy()
        result = True
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        while copied:
            c = copied.popleft()

            if c not in dic:
                stack.append(c)
            else:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    result = False
                    break

        if result and (not copied and not stack):
            answer += 1

    return answer


if __name__ == "__main__":
    s = "[](){}"
    print(solution(s))
