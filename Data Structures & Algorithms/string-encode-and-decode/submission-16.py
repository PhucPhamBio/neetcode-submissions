class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(["{:4}{}".format(len(s),s) for s in strs])

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            length = int(s[i:i+4])
            i      = i + 4
            ans.append(s[i:i+length])
            i      = i + length
        print(ans)
        return ans