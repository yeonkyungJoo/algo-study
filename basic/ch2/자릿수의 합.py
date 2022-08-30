import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))

def digit_sum(x):
    _nums = []
    while x > 0:
        _nums.append(x % 10)
        x //= 10
    return sum(_nums)

answer = 0
for num in nums:
    if digit_sum(answer) < digit_sum(num):
        answer = num
print(answer)