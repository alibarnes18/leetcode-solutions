# 2818. Apply Operations to Maximize Score

## Problem

You are given an array `nums` and an integer `k`.

For each operation:
- Choose a non-empty subarray that has not been chosen before
- Select the element with the highest prime score
- If multiple elements have the same prime score, choose the leftmost one
- Multiply your score by that element

Return the maximum possible score modulo `1e9 + 7`.

---

# Intuition

Instead of generating all subarrays, we calculate:

> How many subarrays choose `nums[i]` as the winning element.

If an element can win `cnt` subarrays, then we can use it at most `cnt` times.

To maximize the answer:
- Use larger numbers first
- Greedily multiply while `k > 0`

---

# Key Observations

## Prime Score

The prime score of a number is:

> Number of distinct prime factors.

Examples:
- `8 = 2³` → score = `1`
- `12 = 2² × 3` → score = `2`

We compute this efficiently using a **Smallest Prime Factor (SPF) sieve**.

---

# Monotonic Stack

For each index `i`, we determine:
- previous index with prime score `>= current`
- next index with prime score `> current`

This correctly handles:
- maximum prime score
- leftmost tie-breaking rule

Then the number of subarrays where `nums[i]` wins is:

```math
(i - left[i]) \times (right[i] - i)