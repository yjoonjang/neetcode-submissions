from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        output = []

        for string in strs:
            string_count_tuple = tuple(sorted(Counter(string).items()))
            if string_count_tuple in groups:
                groups[string_count_tuple].append(string)
            else:
                groups[string_count_tuple] = [string]
        
        return list(groups.values())