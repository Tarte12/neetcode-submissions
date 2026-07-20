class Solution:
    def encode(self, strs: List[str]) -> str:
        txt = "@5#"
        encoding = ""
        for i in strs:
            encoding += i
            encoding += txt
        return encoding


    def decode(self, s: str) -> List[str]:
        decoding = list(map(str, s.split("@5#")))
        return decoding[:-1]
