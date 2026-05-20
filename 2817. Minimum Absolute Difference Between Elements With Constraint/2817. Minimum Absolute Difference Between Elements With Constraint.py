from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums, x):
        sl = SortedList()
        ans = float('inf')

        for i in range(x, len(nums)):
            sl.add(nums[i - x])

            pos = sl.bisect_left(nums[i])

            # sağ komşu
            if pos < len(sl):
                ans = min(ans, abs(nums[i] - sl[pos]))

            # sol komşu
            if pos > 0:
                ans = min(ans, abs(nums[i] - sl[pos - 1]))

        return ans