def solution(s):
    s_list = list(s)
    for i, c in enumerate(s_list):
        if c.isalpha():
            if i == 0 or s_list[i - 1] == ' ':
                s_list[i] = s_list[i].upper()
            else:
                s_list[i] = s_list[i].lower()

    return ''.join(s_list)