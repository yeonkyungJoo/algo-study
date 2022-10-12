def solution(prices):
    answer = [0 for _ in range(len(prices))]

    stack = []
    for i, price in enumerate(prices):

        while stack and prices[stack[-1]] > price:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    while stack:
        idx = stack.pop()
        answer[idx] = (len(prices) - 1) - idx
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))