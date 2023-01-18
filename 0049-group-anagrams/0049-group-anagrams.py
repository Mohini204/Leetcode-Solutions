class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list) #using defaultdict to avoid key error w empty strs

        for word in strs:
            count = [0]*27
            for c in word:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(word)


        return ans.values()


