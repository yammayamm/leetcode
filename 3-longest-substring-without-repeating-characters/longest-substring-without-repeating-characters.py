class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_lenght = 0
        set_ = set()

        for right in range(len(s)):
            while s[right] in set_:
                set_.remove(s[left])
                left += 1

            set_.add(s[right])
            max_lenght = max(max_lenght, right - left + 1)
        return max_lenght