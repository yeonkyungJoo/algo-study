if __name__ == "__main__":
    # [from, to]
    # _input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    _input = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    dic = dict()
    for src, dst in _input:
        # print(src, dst)
        if src not in dic:
            dic[src] = []
        dic[src].append(dst)
        dic[src].sort()
    # print(dic)

    answer = []
    def dfs(s):

        answer.append(s)
        if s in dic:
            for k in dic[s]:
                dic[s].remove(k)
                dfs(k)

    dfs('JFK')
    print(answer)