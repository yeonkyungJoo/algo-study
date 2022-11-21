from collections import deque
'''
def solution(board, moves):
    stack = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2     
                break

    return answer

'''
def solution(board, moves):

    dolls = [deque([]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                dolls[j].appendleft(board[i][j])

    answer = 0
    tmp = []
    for move in moves:
        if not dolls[move-1]:
            continue
        k = dolls[move-1].pop()
        if tmp and tmp[-1] == k:
            tmp.pop()
            answer += 2
        else:
            tmp.append(k)
    return answer


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0],
             [0, 0, 1, 0, 3],
             [0, 2, 5, 0, 1],
             [4, 2, 4, 4, 2],
             [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))
