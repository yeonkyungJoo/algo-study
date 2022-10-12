from typing import List
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        re_paragraph = re.sub(r'[^\w]', ' ', paragraph)
        words = [word for word in re_paragraph.lower().split() if word not in banned]
        return Counter(words).most_common(1)[0][0]

if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))