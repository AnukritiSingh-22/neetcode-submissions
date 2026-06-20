class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            encoded_string = "null"
        else:
            encoded_string = "-".join(strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if s=="null":
            decoded_string = []
        else:
            decoded_string = list(s.split("-"))
        return decoded_string