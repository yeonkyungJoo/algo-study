def solution(numbers):

    answer = ''

    if sum(numbers) == 0:
        return '0'

    numbers.sort()
    _numbers = list(map(str, numbers))
    max_len = 4
    tmp = []
    for i, _num in enumerate(_numbers):
        tmp.append((i, _num * max_len))
    tmp.sort(key=lambda x : -int(x[1][:max_len]))
    for i, _num in tmp:
        answer += _numbers[i]
    return answer

if __name__ == "__main__":
    numbers = [0, 0, 0, 0]
    print(solution(numbers))
