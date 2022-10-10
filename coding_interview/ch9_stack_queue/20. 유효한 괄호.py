from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        result = True
        queue = deque(s)
        stack = []
        while queue:
            c = queue.popleft()
            if c not in dic:
                stack.append(c)
            else:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    result = False
                    break

        if stack:
            result = False
        return result

if __name__ == "__main__":
    s = "(]"
    print(Solution().isValid(s))
