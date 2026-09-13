class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        c = s.split()
        c_joined = "".join(c).lower()
        c = ""
        for char in c_joined:
            if char.isalnum():
                c += char
        mid_idx = (len(c)-1) // 2
        if len(c) % 2 != 0:
            prefix = c[:mid_idx]
            suffix = c[mid_idx + 1:]
        else:
            prefix = c[:mid_idx + 1]
            suffix = c[mid_idx + 1:]
        
        if prefix[::-1] == suffix:
            return True
        else:
            return False