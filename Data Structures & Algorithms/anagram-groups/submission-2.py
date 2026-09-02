# from collections import Counter

# class Solution:
#     def isAnagram(s, t):
#         return len(s) == len(t) and Counter(s) == Counter(t)

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = []
#         strs_counters = {}
#         # for i in range(len(strs)):
#         #     isAnagram = False
#         #     if len(anagrams) == 0:
#         #         anagrams.append([strs[i]])
#         #     else:
#         #         for anagram_candidate_list in anagrams:
#         #             if Solution.isAnagram(strs[i], anagram_candidate_list[0]):
#         #                 isAnagram = True
#         #                 anagram_candidate_list.append(strs[i])
#         #         if isAnagram == False:
#         #             anagrams.append([strs[i]])
#         # return anagrams
#         for str in strs:
#             strs_counters[str] = Counter(str)
#         for key, value in strs_counters:

#             # if Counter(str) in counters_visited:
#             #     counters_visited[Counter[str]].append(str)
#             #     anagrams.append(counters_visited[Counter[str]])
#             # else:
#             #     counters_visited[Counter[str]] = [str]

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())
        # sorted_strs = [sorted(str) for str in strs]
        # temp_list = {}
        # anagrams = []
        # for i, str in enumerate(sorted_strs):
        #     if len(anagrams) == 0:
        #         anagrams.append(str)
        #     else:
        #         if tuple(str) not in temp_list:
        #             temp_list[tuple(str)] = [str]
        #         else:
        #             anagrams.append()
