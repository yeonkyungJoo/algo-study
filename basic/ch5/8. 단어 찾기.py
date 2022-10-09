if __name__ == "__main__":
    N = int(input())
    dic = dict()
    for _ in range(N):
        word = input()
        if word not in dic:
            dic[word] = 0
        dic[word] += 1

    for _ in range(N-1):
        word = input()
        dic[word] -= 1

    for k, v in dic.items():
        if v == 1:
            print(k)
            break
