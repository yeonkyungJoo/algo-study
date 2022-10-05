if __name__ == "__main__":
    nums = [1, 2, 3]

    answer = []
    def dfs(start_idx, path):

        answer.append(path)
        # if start_idx == len(nums):
        #     return

        for i in range(start_idx, len(nums)):
            dfs(i+1, path + [nums[i]])
    dfs(0, [])
    print(answer)

'''
    tmp = []
    answer = []
    def dfs(i):

        if i == len(nums):
            answer.append(tmp[:])
            return

        tmp.append(nums[i])
        dfs(i+1)
        tmp.pop()
        dfs(i+1)

    dfs(0)
    print(answer)
'''