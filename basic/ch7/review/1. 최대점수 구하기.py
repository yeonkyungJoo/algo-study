# sys.stdin = open("../input.txt", "rt")

def dfs(i, total_score, total_time, t_score):
    global answer

    if total_time > M:
        return
    answer = max(answer, total_score)
    if i == N:
        return

    if (total - t_score) + total_score <= answer:
        return

    dfs(i + 1, total_score + quiz[i][0], total_time + quiz[i][1], t_score + quiz[i][0])
    dfs(i + 1, total_score, total_time, t_score + quiz[i][0])



if __name__ == "__main__":
    N, M = map(int, input().split())
    quiz = []
    total = 0
    for _ in range(N):
        score, time = map(int, input().split())
        quiz.append((score, time))
        total += score
    ch = [0 for _ in range(N)]
    answer = 0
    dfs(0, 0, 0, 0)
    print(answer)