from collections import deque
def solution(arr):
    answer = []

    arr = deque(arr)
    while arr:
        n = arr.popleft()
        if not answer or answer[-1] != n:
            answer.append(n)

    return answer

if __name__ == "__main__":
    arr = [4, 4, 4, 3, 3]
    print(solution(arr))