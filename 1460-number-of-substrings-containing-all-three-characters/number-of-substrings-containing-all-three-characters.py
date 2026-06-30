class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = count = 0
        freq = [0] * 3
        
        for right in range(len(s)):
            freq[ord(s[right]) - ord("a")] += 1
            while self._has_all_chars(freq):
                count += len(s) - right # 4
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1 # 1
        return count

    def _has_all_chars(self, freq: list) -> bool:
        # Check if we have at least one of each character
        return all(f > 0 for f in freq)