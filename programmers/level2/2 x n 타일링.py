def solution(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    answer = [0 for _ in range(n+1)]
    answer[1] = 1
    answer[2] = 2
    for i in range(3, n+1):
        answer[i] = (answer[i-2] + answer[i-1]) % 1000000007
    return answer[n]

if __name__ == "__main__":
    n = 4
    print(solution(n))