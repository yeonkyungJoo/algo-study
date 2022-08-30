import sys

# sys.stdin = open("../input.txt", "rt")

N = int(input())
for i in range(N):
    answer = 'YES'

    word = input().lower()
    j = 0
    while j < (len(word) // 2):
        if word[j] != word[(j + 1) * -1]:
            answer = 'NO'
            break
        j += 1
    print('#%d %s' % (i + 1, answer))
