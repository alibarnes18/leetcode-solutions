class Solution:
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        result = set()

        for j in range(n):
            if nums[j] == key:
                for i in range(max(0, j - k), min(n, j + k + 1)):
                    result.add(i)

        return sorted(result)