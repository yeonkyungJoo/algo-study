import sys

sys.stdin = open("../../input.txt", "rt")

n = int(input())
time = []
for _ in range(n):
    time.append(tuple(map(int, input().split())))

time.sort(key=lambda x: x[0])
print(time)

