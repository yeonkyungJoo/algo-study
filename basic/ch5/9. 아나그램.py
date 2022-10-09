if __name__ == "__main__":
    word1 = input()
    word2 = input()

    dic = dict()
    for c in word1:
        if c not in dic:
            dic[c] = 0
        dic[c] += 1

    for c in word2:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] -= 1

    answer = 'YES'
    for k, v in dic.items():
        if v != 0:
            answer = 'NO'
            break
    print(answer)
