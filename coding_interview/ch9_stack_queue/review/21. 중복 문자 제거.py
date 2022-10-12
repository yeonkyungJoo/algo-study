from collections import deque
from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        # print(dic)

        stack = []
        queue = deque(s)
        while queue:
            c = queue.popleft()
            dic[c] -= 1
            if c in stack:
                continue
            while stack and dic[stack[-1]] > 0 and ord(stack[-1]) > ord(c):
                stack.pop()
            stack.append(c)

        return ''.join(stack)

if __name__ == "__main__":
    s = "abacb"
    print(Solution().removeDuplicateLetters(s))