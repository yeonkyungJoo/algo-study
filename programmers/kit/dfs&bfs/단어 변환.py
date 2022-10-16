from collections import deque


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    ch = [0 for _ in range(len(words))]
    queue = deque()
    queue.append((begin, 0))
    while queue:

        word, cnt = queue.popleft()
        if word == target:
            answer = cnt
            break

        for i in range(len(ch)):
            if ch[i] == 0:

                n_word = words[i]
                diff = 0
                for k in range(len(word)):
                    if n_word[k] != word[k]:
                        diff += 1
                if diff == 1:
                    ch[i] = 1
                    queue.append((n_word, cnt + 1))

    return answer