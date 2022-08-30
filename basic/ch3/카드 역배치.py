import sys

# sys.stdin = open("../input.txt", "rt")

cards = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())

    # 3 - 0, 1, 2
    for j in range((b - a + 1) // 2):
        cards[(a-1) + j], cards[(b-1) - j] = cards[(b-1) - j], cards[(a-1) + j]
    # tmp = cards.copy()
    # for j in range(b - a + 1):
    #     cards[(a-1) + j] = tmp[(b-1) - j]

for card in cards:
    print(card, end=' ')
