class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxLength = 0
        maxCount = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxCount = max(maxCount, count[s[right]])

            winLength = right - left + 1
            if winLength - maxCount > k:
                count[s[left]] = count[s[left]] - 1
                left = left + 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength