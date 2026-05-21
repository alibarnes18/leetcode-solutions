class Solution:
    def maximumScore(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        # -------- smallest prime factor sieve --------
        MAXA = max(nums)

        spf = list(range(MAXA + 1))

        for i in range(2, int(MAXA ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXA + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # -------- prime scores --------
        ps = [0] * n

        for i, x in enumerate(nums):
            cnt = 0
            prev = 0

            while x > 1:
                p = spf[x]

                if p != prev:
                    cnt += 1
                    prev = p

                x //= p

            ps[i] = cnt

        # -------- left greater/equal --------
        left = [-1] * n
        stack = []

        for i in range(n):
            while stack and ps[stack[-1]] < ps[i]:
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # -------- right greater --------
        right = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and ps[stack[-1]] <= ps[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        # -------- counts --------
        arr = []

        for i in range(n):
            cnt = (i - left[i]) * (right[i] - i)
            arr.append((nums[i], cnt))

        # -------- greedy --------
        arr.sort(reverse=True)

        ans = 1

        for val, cnt in arr:
            if k == 0:
                break

            use = min(k, cnt)

            ans = (ans * pow(val, use, MOD)) % MOD

            k -= use

        return ans