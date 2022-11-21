def solution(number, k):

    stack = []
    for i, c in enumerate(number):
        n = int(c)
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
        if k == 0:
            return ''.join(map(str, stack)) + number[i+1:]

    if k > 0:
        while k > 0:
            stack.pop()
            k -= 1
    return ''.join(map(str, stack))

if __name__ == "__main__":
    number = "20"
    k = 1
    print(solution(number, k))