if __name__ == "__main__":

    _input = [1, 2, 3]
    size = len(_input)
    answer = []
    def dfs(i):

        if i >= size:
            print(answer)
            return

        for k in range(size):
            n = _input[k]
            if n not in answer:
                answer.append(n)
                dfs(i+1)
                answer.pop()

    dfs(0)