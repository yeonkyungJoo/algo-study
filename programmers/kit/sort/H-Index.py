def solution(citations):

    answer = 0
    citations.sort()
    l, r = 0, citations[-1]
    while l < r:
        mid = (l + r) // 2

        up = 0
        for citation in citations:
            if citation >= mid:
                up += 1
        if up >= mid:
            answer = max(answer, mid)
            l += 1
        else:
            r -= 1
    return answer

if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))