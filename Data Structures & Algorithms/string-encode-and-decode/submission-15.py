class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s_str in strs:
            encoded_string += s_str + "##yjoonjang##"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("##yjoonjang##")
        return decoded_strs[:len(decoded_strs)-1]