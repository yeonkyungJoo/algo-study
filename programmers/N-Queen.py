def solution(n):
    queen = [0] * n
    count = 0

    def dfs(queen, row):
        nonlocal count

        if n == row:
            count += 1
            return

        # 가로로 한번만 진행
        for col in range(n):
            queen[row] = col

            # for-else구문
            for x in range(row):
                # 세로로 겹치면 안됨
                if queen[x] == queen[row]:
                    break

                # 대각선으로 겹치면 안됨
                if abs(queen[x] - queen[row]) == (row - x):
                    break
            else:
                dfs(queen, row + 1)

        return count

    dfs(queen, 0)
    return count

if __name__ == "__main__":
    print(solution(4))