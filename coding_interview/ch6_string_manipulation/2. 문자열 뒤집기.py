from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:

        size = len(s)
        i = 0
        while i < (size // 2):
            s[i], s[-i-1] = s[-i-1], s[i]
            i += 1


if __name__ == "__main__":
    s = ["H","a","n","n","a","h"]
    print(Solution().reverseString(s))