class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for elem in strs:
            out += f"{len(elem)}#"
            out += elem
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        idx = 0

        while idx < len(s):
            length = ""
            while s[idx] != "#":
                length += s[idx]
                idx+=1
            length = int(length)
            out_str = ""
            for i in range(length):
                idx += 1
                out_str += s[idx]
            idx += 1
            print(out_str)
            out.append(out_str)
        return out

