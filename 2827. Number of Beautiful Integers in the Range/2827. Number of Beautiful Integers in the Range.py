class Solution:
    def numberOfBeautifulIntegers(self, low, high, k):

        def count(x):
            s = str(x)
            n = len(s)

            memo = {}

            def dp(i, mod, diff, tight, started):
                key = (i, mod, diff, tight, started)

                if key in memo:
                    return memo[key]

                if i == n:
                    return int(started and mod == 0 and diff == 0)

                limit = int(s[i]) if tight else 9
                res = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    nstarted = started or d != 0

                    nmod = mod
                    ndiff = diff

                    if nstarted:
                        nmod = (mod * 10 + d) % k

                        if d % 2 == 0:
                            ndiff += 1
                        else:
                            ndiff -= 1

                    res += dp(i + 1, nmod, ndiff, ntight, nstarted)

                memo[key] = res
                return res

            return dp(0, 0, 0, True, False)

        return count(high) - count(low - 1)