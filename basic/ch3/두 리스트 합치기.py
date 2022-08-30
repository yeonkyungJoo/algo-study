from collections import deque
import sys

# sys.stdin = open("../input.txt", "rt")

N = int(input())
nums1 = deque(map(int, input().split()))
M = int(input())
nums2 = deque(map(int, input().split()))

answer = []
while len(nums1) > 0 and len(nums2) > 0:
    if nums1[0] < nums2[0]:
        answer.append(nums1.popleft())
    else:
        answer.append(nums2.popleft())

if len(nums1) == 0:
    answer.extend(nums2)
else:
    answer.extend(nums1)
for n in answer:
    print(n, end=' ')

