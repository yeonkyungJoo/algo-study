def solution(brown, yellow):
    total = brown + yellow
    # 약수
    nums = []
    for n in range(1, total + 1):
        if total % n == 0:
            nums.append(n)

    # 갈색 세로, 갈색 가로
    bci, bri = 0, len(nums) - 1
    while bci <= bri:
        bc = nums[bci]
        br = nums[bri]

        yc, yr = bc - 2, br - 2
        if yc > 0 and yr > 0 and yc * yr == yellow:
            answer = [br, bc]
            break

        bci += 1
        bri -= 1

    return answer