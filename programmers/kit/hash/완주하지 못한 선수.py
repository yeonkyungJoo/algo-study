def solution(participant, completion):

    dic = dict()
    for p in participant:
        if p not in dic:
            dic[p] = 0
        dic[p] += 1

    for c in completion:
        dic[c] -= 1

    for k, v in dic.items():
        if v != 0:
            answer = k
            break

    return answer


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))
