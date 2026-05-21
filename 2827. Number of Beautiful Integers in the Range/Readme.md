# 2818. Apply Operations to Maximize Score

##  Problem

You are given an array `nums` and an integer `k`.

You can perform at most `k` operations:

- Choose a non-empty subarray (each subarray can be used only once)
- Select the element with the highest prime score
- If tied, choose the leftmost element
- Multiply your score by that element

Return the maximum score modulo `1e9 + 7`.

---

##  Key Idea

Instead of checking all subarrays:

> We compute how many subarrays each index can "win".

So each `nums[i]` contributes multiple times depending on how many subarrays select it.

---

##  Core Insight

For each index `i`:

- Find how far it can extend to the left (previous higher/equal prime score)
- Find how far it can extend to the right (next strictly higher prime score)

Then:

```
contribution[i] = (i - left[i]) * (right[i] - i)
``` id="r2"

This gives the number of subarrays where `nums[i]` is selected.

---

##  Approach

### 1. Prime Score
Compute number of distinct prime factors for each element.

---

### 2. Monotonic Stack
Used to find:
- Previous greater/equal element
- Next greater element

This handles tie-breaking rule (leftmost index).

---

### 3. Contribution Calculation
Each index gets a frequency = number of subarrays where it is chosen.

---

### 4. Greedy Strategy
Sort numbers in descending order and use highest values first.

Apply at most `k` times.

---

##  Complexity

```
Time Complexity: O(n log n)
Space Complexity: O(n)
``` id="r3"

---

##  Files Structure

```
/solution.py   → main algorithm
/README.md     → explanation
``` id="r4"

---

##  Summary

- Transform subarray problem → frequency counting problem
- Use monotonic stack to compute contribution range
- Greedy multiply largest values first