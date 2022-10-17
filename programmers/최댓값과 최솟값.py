def solution(s):
    nums = []
    splits = s.split(' ')
    for k in splits:
        n = int(k)
        nums.append(n)
    nums.sort()

    return str(nums[0]) + ' ' + str(nums[-1])