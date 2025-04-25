# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest = 0, 0
        chars = set()

        for r in range(len(s)):
            # if new index in set, keep removing
            while s[r] in chars:
                chars.remove(s[left])
                left += 1

            # then add new index
            chars.add(s[r])
            # update longest
            longest = max(longest, r - left + 1)

        return longest
