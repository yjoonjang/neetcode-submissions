import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = s.split()
        c_joined = "".join(c).lower()
        result = re.sub(r"[^a-zA-Z0-9]", "", c_joined)
        if len(result) % 2 != 0:
            mid = len(result) // 2
            for i in range(0, mid):
                if result[mid-i-1] != result[mid+i+1]:
                    return False
            return True
        else:
            mid = len(result) % 2 + len(result) // 2
            for i in range(0, mid):
                if result[mid-i-1] != result[mid+i]:
                    return False
            return True