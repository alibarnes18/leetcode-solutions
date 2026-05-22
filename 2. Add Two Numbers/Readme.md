# 🔢 Add Two Numbers (LeetCode #2)

##  Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

---

##  Approach
We simulate the addition process like manual arithmetic:

- Traverse both linked lists
- Add corresponding digits
- Keep track of carry
- Create a new linked list for the result

---

##  Algorithm
1. Initialize a dummy node
2. Loop while `l1`, `l2`, or `carry` exists
3. Compute sum = l1 + l2 + carry
4. Create new node with `sum % 10`
5. Update carry = `sum // 10`
6. Move pointers forward

---

##  Complexity Analysis
- **Time Complexity:** O(max(n, m))
- **Space Complexity:** O(max(n, m))

---

