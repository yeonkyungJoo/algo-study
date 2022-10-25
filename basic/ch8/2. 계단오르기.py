if __name__ == "__main__":
    N = int(input())

    def func(n):

        if ch[n] > 0:
            return ch[n]

        ch[n] = func(n-1) + func(n-2)
        return ch[n]

    ch = [0 for _ in range(N+1)]
    ch[1] = 1
    ch[2] = 2
    print(func(N))