def solution(survey, choices):
    answer = ''
    dic = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }

    for i in range(len(choices)):
        choice = choices[i]
        if choice < 4:
            dic[survey[i][0]] += abs(choice - 4)
        elif choice > 4:
            dic[survey[i][1]] += abs(choice - 4)

    for t1, t2 in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        answer += (t1 if dic[t1] >= dic[t2] else t2)

    return answer

if __name__ == "__main__":
    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    print(solution(survey, choices))