def solution(numbers, hand):
    answer = ''

    map = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2),
    }

    l, r = '*', '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            l = number
        elif number in [3, 6, 9]:
            answer += 'R'
            r = number
        else:
            l_diff = abs(map[number][0] - map[l][0]) + abs(map[number][1] - map[l][1])
            r_diff = abs(map[number][0] - map[r][0]) + abs(map[number][1] - map[r][1])
            if l_diff == r_diff:
                if hand == 'left':
                    answer += 'L'
                    l = number
                else:
                    answer += 'R'
                    r = number
            else:
                if l_diff < r_diff:
                    answer += 'L'
                    l = number
                else:
                    answer += 'R'
                    r = number
    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))