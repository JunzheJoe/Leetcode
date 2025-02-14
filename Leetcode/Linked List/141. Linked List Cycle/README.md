# 141. Linked List Cycle

🔗 **[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Linked List, Two Pointers, Floyd's Cycle Detection  

---

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

**Return `true` if there is a cycle in the linked list. Otherwise, return `false`.**

**Note:** This problem could have **duplicate values for different nodes**, meaning multiple nodes can store the same value but still be distinct nodes.

---

## Examples

### Example 1:
**Input:**  
```python
head = [3,2,0,-4]
pos = 1
```
**Output:**  
```python
True
```
**Explanation:**  
There is a cycle in the linked list where the tail connects to the second node.

### Example 2:
**Input:**  
```python
head = [1,2]
pos = 0
```
**Output:**  
```python
True
```
**Explanation:**  
There is a cycle in the linked list where the tail connects to the first node.

### Example 3:
**Input:**  
```python
head = [1]
pos = -1
```
**Output:**  
```python
False
```
**Explanation:**  
There is no cycle in the linked list.

---

## Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- We need to determine if a cycle exists in a linked list.
- A cycle occurs if a node is visited more than once when traversing the list.
- **Important Note:** Different nodes may have the **same value** but still be **distinct nodes**.
- **Happy Path Test:** `[3,2,0,-4]`, `pos = 1` → Output: `True`
- **Edge Cases:** 
  - Empty list (`head = None`) → `False`
  - Single node, no cycle (`[1], pos = -1`) → `False`
  - Single node, cycle (`[1], pos = 0`) → `True`

---

### 2️⃣ Match
- **Problem Category:** Linked Lists, Two Pointers.  
- **Pattern:** Floyd’s Tortoise and Hare Algorithm.  
  - `slow` moves one step per iteration.  
  - `fast` moves two steps per iteration.  
- If there is a cycle, `slow` and `fast` will eventually meet.  

---

### 3️⃣ Plan (Floyd’s Tortoise and Hare Algorithm)
- **Idea:** Use Floyd's cycle detection algorithm.  
- **Why does `slow` meet `fast` in a cycle?**  
  - Each iteration reduces the distance between `slow` and `fast` by one.  
  - If the list length is `n`, in the worst case, it takes `O(n)` iterations for `fast` to catch `slow`.  
![alt text](<Floyd's Tortoise & Hare.png>)
- **Pseudocode:**  
  ```
  1. Initialize slow and fast pointers to head.
  2. While fast and fast.next are not None:
      a. Move slow one step.
      b. Move fast two steps.
      c. If slow == fast: return True (cycle detected)
  3. Return False (no cycle)
  ```

---

### 4️⃣ Implement
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next            # Slow pointer moves one step
            fast = fast.next.next       # Fast pointer moves two steps
            if slow == fast:
                return True             # Cycle detected
        
        return False                    # No cycle
```

---

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `[3,2,0,-4]`, `pos = 1` → Output: `True` (Cycle detected)  
- ✅ **Test with Edge Cases:**  
  - Input: `[]` → Output: `False`  
  - Input: `[1]`, `pos = -1` → Output: `False`  
  - Input: `[1,2]`, `pos = 0` → Output: `True`  
- ✅ **Check for Logic Bugs:** Carefully ensured pointers advance correctly.  
- ✅ **Run Debugging Steps:** Walked through iterations to confirm logic.  

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - In the worst case, both pointers traverse the entire list.  
- **Space Complexity:** `O(1)`  
  - Only two pointers (`slow` and `fast`) are used.  

**Pros:**  
- Efficient `O(N)` time with `O(1)` space.  
- Works well on large lists.  

**Cons:**  
- May be less intuitive than using a set to track visited nodes.  

---

## 📝 Related Problems
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) – Find the node where the cycle begins.  
- [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) – Cycle detection in arrays.  
