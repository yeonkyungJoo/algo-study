def solution(s):
    answer = 1
    for i in range(len(s)):

        for j in range(i + 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                answer = max(answer, j - i + 1)
    return answer