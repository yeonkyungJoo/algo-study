def solution(arr1, arr2):

    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):

            r = arr1[i][:]
            c = []
            for k in range(len(arr2)):
                c.append(arr2[k][j])

            value = 0
            for m, n in zip(r, c):
                value += m * n
            answer[i][j] = value

    return answer