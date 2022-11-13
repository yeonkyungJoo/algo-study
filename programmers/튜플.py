def solution(s):
    answer = []

    map = dict()
    nums_str = ''
    for i in range(len(s)):
        c = s[i]
        if c in ('{', '}'):
            continue
        nums_str += c
    nums = nums_str.split(',')
    for num in nums:
        n = int(num)
        if n not in map:
            map[n] = 0
        map[n] += 1
    items = list(map.items())
    items.sort(key=lambda x : -x[1])

    for k, v in items:
        answer.append(k)
    return answer

if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))