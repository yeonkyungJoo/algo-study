# sys.stdin = open("../input.txt", "rt")
import sys


def dfs(i, decrypted):
    global cnt

    if i >= len(code):
        cnt += 1
        print(decrypted)
        return

    if code[i] == '0':
        return

    _code = int(code[i])
    if 1 <= _code <= 26:
        dfs(i + 1, decrypted + alphabet[_code - 1])

    if i + 1 < len(code):
        _code = int(code[i:i+2])
        if 1 <= _code <= 26:
            dfs(i + 2, decrypted + alphabet[_code - 1])


if __name__ == "__main__":
    code = input()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cnt = 0
    dfs(0, '')
    print(cnt)
