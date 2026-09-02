class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[]"
        results = ""
        for s in strs:
            results += str(len(s)) + "#yjoonjang" + s
        return results

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        decoded_results = []
        next_str_num = 0
        for i, small_s in enumerate(s.split("#yjoonjang")):
            if i == 0:
                next_str_num = int(small_s)
            if (i != 0) & (i < len(s.split("#yjoonjang")) - 1):
                decoded_results.append(small_s[:next_str_num])
                next_str_num = int(small_s[next_str_num:])
            if i == len(s.split("#yjoonjang")) - 1:
                decoded_results.append(small_s)
        
        return decoded_results