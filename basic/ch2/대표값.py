import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
scores = list(map(int, input().split()))

average = round(sum(scores) / len(scores))
_answer = (0, scores[0])
for idx, score in enumerate(scores):
    comp = abs(score - average) - abs(_answer[1] - average)
    if comp < 0:
        _answer = (idx, score)
    elif comp == 0:
        if score > _answer[1]:
            _answer = (idx, score)
print(average, _answer[0] + 1)
