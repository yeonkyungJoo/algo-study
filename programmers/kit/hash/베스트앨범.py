def solution(genres, plays):
    answer = []

    size = len(genres)
    dic = dict()
    for i in range(size):
        genre = genres[i]
        play = plays[i]
        if genre not in dic:
            dic[genre] = [0, []]
        dic[genre][0] += play
        dic[genre][1].append((i, play))

    values = list(dic.values())
    values.sort(key=lambda x : -x[0])
    for total, _list in values:

        for i in range(2):
            _list.sort(key=lambda x: -x[1])
            if _list:
                idx, cnt = _list.pop(0)
                answer.append(idx)

    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))