if __name__ == "__main__":

    n = 5
    k = 3

    answer = []
    def dfs(i, start):

        if i == k:
            print(answer)
            return

        for m in range(start, n+1):
            if m not in answer:
                answer.append(m)
                dfs(i+1, m+1)
                answer.pop()
    dfs(0, 1)
