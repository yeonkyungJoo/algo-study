import math
def solution(numbers):

    def isPrime(n):

        if n < 2:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def dfs(idx, number):

        if idx == len(numbers):
            n = int(number)
            if isPrime(n):
                _set.add(n)
            return

        for i in range(len(_numbers)):
            if ch[i] == 0:
                ch[i] = 1
                dfs(idx + 1, number + _numbers[i])
                ch[i] = 0

    _set = set()
    _numbers = list(numbers)
    _numbers.append("")
    ch = [0 for _ in range(len(_numbers))]
    dfs(0, '')
    return len(_set)

if __name__ == "__main__":
    numbers = "17"
    print(solution(numbers))