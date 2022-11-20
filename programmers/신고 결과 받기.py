def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report = list(set(report))

    count = dict()
    report_map = dict()
    for r in report:
        user_id, reported_user_id = r.split()
        if reported_user_id not in count:
            count[reported_user_id] = 0
        count[reported_user_id] += 1

        if user_id not in report_map:
            report_map[user_id] = []
        report_map[user_id].append(reported_user_id)

    for user, reported_users in report_map.items():
        for reported_user in reported_users:
            if count[reported_user] >= k:
                answer[id_list.index(user)] += 1
    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))