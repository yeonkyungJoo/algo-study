def solution(N, stages):
    stages.sort()
    # 1, 2, 2, 2, 3, 3, 4, 6
    # >= 1 : 8 / 1
    # >= 2 : 7 / 3
    # >= 3 : 4 / 2
    # >= 4 : 2 / 1
    # >= 5 : 1 / 0

    count = [0 for _ in range(N+1)]
    total = [0 for _ in range(N+1)]
    stage = 1
    idx = 0
    while idx < len(stages):
        if stage <= N and stage <= stages[idx]:
            total[stage] = len(stages) - idx
            stage += 1
        if stages[idx] <= N:
            count[stages[idx]] += 1
        idx += 1

    answer = []
    for i, (c, t) in enumerate(zip(count, total)):
        if i == 0:
            continue
        if t == 0:
            answer.append((i, 0))
        else:
            answer.append((i, c / t))
    answer.sort(key=lambda x: (-x[1], x[0]))
    return [x[0] for x in answer]

if __name__ == "__main__":
    N = 4
    stages = [4, 4, 4, 4, 4]
    print(solution(N, stages))