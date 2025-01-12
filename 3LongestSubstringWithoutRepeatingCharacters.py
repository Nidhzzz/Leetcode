class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr1, count = 0, 0 
        seen = {}
        for idx, char in enumerate(s):
            if char in seen and seen[char] + 1 > ptr1:
                ptr1 = seen[char] + 1
            seen[char] = idx
            count = max(idx - ptr1 + 1, count)
        return count