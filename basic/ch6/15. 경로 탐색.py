# sys.stdin = open("../input.txt", "rt")

def dfs(i):
    global cnt

    if i == N - 1:
        cnt += 1

        for p in path:
            print(p + 1, end=' ')
        print()
        return

    for j in range(N):
        if i != j and ch[j] == 0 and arr[i][j] == 1:
            ch[j] = 1
            path.append(j)
            dfs(j)
            path.pop()
            ch[j] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        s, e = map(int, input().split())
        arr[s - 1][e - 1] = 1
    cnt = 0
    path = [0]
    ch = [0 for _ in range(N)]
    ch[0] = 1
    dfs(0)
    print(cnt)

'''       
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
'''
