class Solution:
    def isPalindrome(self, s: str) -> bool:

        tmp = []
        for c in s:
            if c.isalnum():
                tmp.append(c.lower())

        return tmp == tmp[::-1]

if __name__ == "__main__":
    s = " "
    print(Solution().isPalindrome(s))