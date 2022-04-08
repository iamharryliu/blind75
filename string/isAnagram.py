class Solution:
    @classmethod
    def isAnagram(self, s, t):
        dic1, dic2 = {}, {}
        # loop through strings and increment counter for characters
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        # check that dics are the same
        return dic1 == dic2


s = "anagram"
t = "nagaram"

result = Solution.isAnagram(s, t)
print(result)
