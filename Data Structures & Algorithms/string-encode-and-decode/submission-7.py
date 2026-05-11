class Solution:

    def encode(self, strs: List[str]) -> str:
        return ":;".join(strs) if len(strs) else None

    def decode(self, s: str) -> List[str]:
        return s.split(":;") if s is not None else []
