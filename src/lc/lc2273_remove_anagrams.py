# Leetcode 2273 Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        out = []
        prev = "" # Note adjacency constraint 
        for i in range(0, len(words)):
            alphabetical = "".join(sorted(words[i]))
            if alphabetical != prev:
                out.append(words[i])
            prev = alphabetical
        return out


# Another adjacency constraint problem:
    # Leetcode 3349. Adjacent Increasing Subarrays Detection I