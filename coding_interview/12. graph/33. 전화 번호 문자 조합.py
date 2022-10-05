if __name__ == "__main__":
    phone = {
        1: [],
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']
    }

    answer = []
    def dfs(i, word):

        if i >= len(_input):
            # print(word)
            answer.append(word)
            return

        for c in phone[int(_input[i])]:
            dfs(i+1, word + c.lower())

    _input = list(input())
    dfs(0, '')
    print(answer)