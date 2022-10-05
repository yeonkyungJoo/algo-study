def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        prev = phone_book[i]
        next = phone_book[i+1]
        if prev == next[0:len(prev)]:
            answer = False
    return answer


if __name__ == "__main__":
    phone_book = ["12", "1312"]
    print(solution(phone_book))
