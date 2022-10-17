def solution(n):

    answer = 0

    # 동적계획법
    ch = [0 for _ in range(n+1)]
    ch[1] = 1
    for i in range(2, n+1):
        ch[i] = ch[i-2] + ch[i-1]
    return ch[n] % 1234567

'''
def solution(n):

    def F(k):
        if k <= 1:
            return k

        if ch[k] == 0:
            ch[k] = F(k - 2) + F(k - 1)
        return ch[k]

    ch = [0 for _ in range(100001)]
    return F(n) % 1234567
'''

if __name__ == "__main__":
    print(solution(100000))