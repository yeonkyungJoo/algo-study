if __name__ == "__main__":
    n = 2
    course = [[1, 0], [0, 1]]

    dic = dict()
    for c in course:
        start, end = c
        if start not in dic:
            dic[start] = []
        dic[start].append(end)
    # print(dic)

    answer = True
    traced = set()
    visited = set()
    def dfs(i):

        if i in traced:
            return False

        if i in visited:
            return True

        traced.add(i)
        for y in dic[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        visited.add(i)

        return True

    for x in list(dic):
        if not dfs(x):
            answer = False
    print(answer)

