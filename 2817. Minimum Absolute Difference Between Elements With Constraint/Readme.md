# 2817. Minimum Absolute Difference Between Elements With Constraint

🔗 https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

## Difficulty
Medium

---

## Approach

Maintain a sorted structure of elements that are at least `x` indices apart.

For each current element:
- insert the valid previous element into a `SortedList`
- use binary search to find the closest value
- minimize the absolute difference

This reduces the brute-force O(n²) solution to O(n log n).

---

## Key Concepts
- SortedList
- Binary Search
- Ordered Set
- Sliding Window Constraint

---

## Complexity
- Time: O(n log n)
- Space: O(n)

---

## Performance
- Runtime: 979 ms (Beats 44.00%)
- Memory: 22.24 MB (Beats 56.00%)

---

## Pattern
Closest value search in a sorted structure.