from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for str in strs:
            _str = ''.join(sorted(str.lower()))
            if _str not in dic:
                dic[_str] = []
            dic[_str].append(str)
        return list(dic.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))