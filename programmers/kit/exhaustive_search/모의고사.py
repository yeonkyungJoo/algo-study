def solution(answers):
    solve = [[1, 2, 3, 4, 5],
             [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    correct = [0, 0, 0]
    for i in range(len(answers)):
        answer = answers[i]

        for k in range(3):
            if answer == solve[k][i % len(solve[k])]:
                correct[k] += 1

    correct = [(i+1, c) for i, c in enumerate(correct)]
    correct.sort(key=lambda x : (-x[1], x[0]))
    max_correct = max(correct, key=lambda x : x[1])[1]

    rv = []
    for i, c in correct:
        if c == max_correct:
            rv.append(i)
    return rv

if __name__ == "__main__":
    answers = [1, 2, 3, 4, 5]
    print(solution(answers))