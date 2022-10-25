if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    dy = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                dy[i] = max(dy[i], dy[j] + 1)
    print(max(dy))