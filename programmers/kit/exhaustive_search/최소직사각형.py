import sys
def solution(sizes):

    max_x, max_y = -sys.maxsize, -sys.maxsize
    for size in sizes:
        x, y = max(size), min(size)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return max_x * max_y

if __name__ == "__main__":
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))