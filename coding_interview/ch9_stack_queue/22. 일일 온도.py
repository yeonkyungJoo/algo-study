from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer =  [0 for _ in range(len(temperatures))]
        queue = deque([(i, t) for i, t in enumerate(temperatures)])
        stack = []

        while queue:
            idx, temperature = queue.popleft()

            while stack and stack[-1][1] < temperature:
                last = stack.pop()
                answer[last[0]] = idx - last[0]
            stack.append((idx, temperature))
        return answer

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))
