import sys

# sys.stdin = open("../input.txt", "rt")

s = input()
nums = []
for c in s:
    if c.isnumeric():
        nums.append(c)
num = int(''.join(nums))
print(num)

i = 1
cnt = 0
while i <= num:
    if num % i == 0:
        cnt += 1
    i += 1
print(cnt)