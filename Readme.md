# 2200. Find All K-Distant Indices in an Array

🔗 https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

## Difficulty
Easy

---

## Approach

For each index containing `key`, expand the range `[j - k, j + k]` and mark all valid indices.

A set is used to avoid duplicates, and the final result is sorted.

---

## Key Idea
- Find all positions of `key`
- Expand ±k range around each position
- Use a set to avoid duplicates

---

## Complexity
- Time: O(n * k) worst case
- Space: O(n)

---

## Performance (LeetCode)
- Runtime: 307 ms (Beats 48.89%)
- Memory: 12.55 MB (Beats 57.78%)

---

## Pattern
- Range Expansion
- Brute force marking