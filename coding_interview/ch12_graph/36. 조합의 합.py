if __name__ == "__main__":

    candidates = [2, 3, 5]
    target = 8

    answer = []
    tmp = []
    def dfs(start_idx, sum):

        if sum > target:
            return
        if sum == target:
            answer.append(tmp.copy())
            return

        for i in range(start_idx, len(candidates)):
            n = candidates[i]
            tmp.append(n)
            dfs(i, sum + n)
            tmp.pop()

    dfs(0, 0)
    print(answer)



