#from collections import deque


def solution(n):
    answer = []

    def recursive(n, src, mid, dst):
        if n <= 0:
            return

        recursive(n - 1, src, dst, mid)
        answer.append([src, dst])
        recursive(n - 1, mid, src, dst)

    recursive(n, 1, 2, 3)

    return answer

if __name__ == "__main__":
    print(solution(3))