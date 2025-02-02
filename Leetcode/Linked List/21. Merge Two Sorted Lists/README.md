# 21. Merge Two Sorted Lists

🔗 **[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Linked List, Two Pointers  

---

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list by **splicing together the nodes** of the first two lists.

Return the **head** of the merged linked list.

---

## Examples

### Example 1:
**Input:**  
```python
list1 = [1,2,4]
list2 = [1,3,4]
```
**Output:**  
```python
[1,1,2,3,4,4]
```

### Example 2:
**Input:**  
```python
list1 = []
list2 = []
```
**Output:**  
```python
[]
```

### Example 3:
**Input:**  
```python
list1 = []
list2 = [0]
```
**Output:**  
```python
[0]
```

---

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. Can the input be empty (head is `None`)?  
   - Yes, either list can be empty.
2. Any requirement on time/space complexity?  
   - **O(N + M) time** and **O(1) space** (merge in place).  
3. Does the linked list have cycles?  
   - No.
4. Can the input lists have differing lengths?  
   - Yes, do not assume they have the same length.

### 2️⃣ Match
This is a **Linked List** problem, so consider:
- **Dummy Head**: Simplifies handling of the merged list.
- **Two Pointers**: One for each list to traverse and merge nodes in sorted order.

### 3️⃣ Plan
1. Create a **dummy node** (`dummy = ListNode(0)`) to act as the starting point.
2. Use a **pointer `tail`** to build the merged list.
3. Iterate while both lists are **not empty**:
   - Compare `list1.val` and `list2.val`.
   - Attach the smaller node to `tail.next` and move the pointer forward.
   - Move `tail` forward.
4. If one list is **not empty**, attach the remaining part to `tail.next`.
5. Return `dummy.next` as the head of the merged list.

---

## 4️⃣ Implementation
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the number of nodes in `list1` and `M` is the number of nodes in `list2`.

- **Time Complexity:** `O(N + M)`  
  - We traverse each list once.
- **Space Complexity:** `O(1)` (merge in place)  
  - No extra space is used, only pointers are updated.

---

## 6️⃣ Additional Notes
- Using a **dummy node** simplifies list handling and avoids extra conditions (e.g., either of the lists can be empty).
- This solution **modifies the input lists in place**, making it efficient.

---

## 📝 Related Problems
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [148. Sort List](https://leetcode.com/problems/sort-list/)
