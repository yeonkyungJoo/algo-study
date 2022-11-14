def solution(relation):

    rows = len(relation)
    cols = len(relation[0])
    keys_list = []
    def dfs(idx, start, keys):

        keys_list.append(keys)
        if idx == cols + 1:
            return
        for key in range(start+1, cols):
            dfs(idx+1, key, keys + str(key))

    dfs(0, -1, '')
    keys_list.sort(key=lambda x : len(x))
    answer = []
    for keys in keys_list:

        for a in answer:
            if keys.find(a) >= 0:
                break
        else:
            _set = set()
            for r in relation:
                v = ''
                for i in keys:
                    v += r[int(i)]
                _set.add(v)
            if len(_set) == rows:
                answer.append(keys)

    return len(answer)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    print(solution(relation))