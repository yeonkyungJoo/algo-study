from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isnumeric():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits

if __name__ == "__main__":
    logs = ["dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero"]
    print(Solution().reorderLogFiles(logs))
