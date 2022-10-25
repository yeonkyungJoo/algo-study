if __name__ == "__main__":
    N = int(input())

    ch = [0 for _ in range(N+1)]
    ch[0] = 1
    ch[1] = 2
    for i in range(2, N+1):
        ch[i] = ch[i-1] + ch[i-2]
    print(ch[N])