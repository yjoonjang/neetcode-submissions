class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [char for char in s]

        containsSameChar = False
        appearsSameTime = False

        characters_in_s = set(s)
        characters_in_t = set(t)

        if characters_in_s == characters_in_t:
            containsSameChar = True
            for char in characters_in_s:
                if (s.count(char) != t.count(char)):
                    appearsSameTime = False
                    break
                else:
                    appearsSameTime = True
        
        if containsSameChar and appearsSameTime:
            return True
        else:
            return False
                

#         # if containsSameChar and 

# s = "racecar"
# t = "carrace"
# s_list = [char for char in s]
# t_list = [char for char in t]
# s_set = set(s_list)
# t_set = set(t_list)
# print(s_list)
# print(s_set)
# print(t_set)
# print(s_set == t_set)
# for char in s_set:
#     print(char, s.count(char))