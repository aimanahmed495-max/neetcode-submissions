class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        frequency = []
        for i in range(len(nums) + 1):
            frequency.append([])

        for num, cnt in count.items():
            frequency[cnt].append(num)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result
