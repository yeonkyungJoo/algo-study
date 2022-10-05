def solution(clothes):

    dic = dict()
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 0
        dic[kind] += 1

    answer = 1
    for v in dic.values():
        answer *= (v + 1)

    return answer - 1


if __name__ == "__main__":
    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))
