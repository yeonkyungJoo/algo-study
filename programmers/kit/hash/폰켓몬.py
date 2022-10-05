def solution(nums):
    _set = set(nums)
    return (len(nums) // 2) if len(_set) >= (len(nums) // 2) else len(_set)


if __name__ == "__main__":
    nums = [3, 3, 3, 2, 2, 2]
    print(solution(nums))
