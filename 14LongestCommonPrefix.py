class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        smallest = min(strs, key=len)

        for i in range(len(smallest)):
            for s in strs:
                if s[i] != smallest[i]:
                    return "".join(res)
            res.append(s[i])

        return "".join(res)