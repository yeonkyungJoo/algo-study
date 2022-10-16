def solution(word):
    words = []

    def dfs(idx, string):

        words.append(string)
        if idx == 5:
            return

        for c in ['A', 'E', 'I', 'O', 'U']:
            dfs(idx + 1, string + c)

    dfs(0, '')

    for i, _word in enumerate(words):
        if word == _word:
            answer = i
    return answer