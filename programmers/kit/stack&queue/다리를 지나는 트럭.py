from collections import deque


def solution(bridge_length, weight, truck_weights):

    time = 0
    on_bridge = deque()
    now = 0
    for i in range(len(truck_weights)):

        truck_weight = truck_weights[i]

        time += 1
        while now + truck_weight > weight:
            t, w = on_bridge.popleft()
            time = t + bridge_length
            now -= w
        on_bridge.append((time, truck_weight))
        now += truck_weight

    while on_bridge:
        time = on_bridge.popleft()[0] + bridge_length
    return time


if __name__ == "__main__":
    bridge_length = 5
    weight = 5
    truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
    print(solution(bridge_length, weight, truck_weights))
