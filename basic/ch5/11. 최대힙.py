import heapq

if __name__ == "__main__":
    nums = []
    while True:
        n = int(input())
        if n == -1:
            break

        if n > 0:
            heapq.heappush(nums, n * (-1))
        elif n == 0:
            print(heapq.heappop(nums) * (-1))
