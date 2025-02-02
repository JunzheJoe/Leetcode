# 20. Valid Parentheses

🔗 **[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Stack, String  

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.

A string is **valid** if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every closing bracket must have a corresponding opening bracket.

---

## Examples

### Example 1:
**Input:**  
```python
s = "()"
```
**Output:**  
```python
True
```

### Example 2:
**Input:**  
```python
s = "()[]{}"
```
**Output:**  
```python
True
```

### Example 3:
**Input:**  
```python
s = "(]"
```
**Output:**  
```python
False
```

### Example 4:
**Input:**  
```python
s = "([)]"
```
**Output:**  
```python
False
```

### Example 5:
**Input:**  
```python
s = "{[]}"
```
**Output:**  
```python
True
```

---

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of only the characters `()[]{}`.

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. Can the input string be empty?
   - No, the constraints specify `s.length >= 1`.
2. Can an opening bracket appear inside another bracket?
   - Yes, valid nesting is allowed.
3. Any requirement on time/space complexity?
   - The optimal solution should run in **O(N) time** with **O(N) space**.

### 2️⃣ Match
- This problem can be efficiently solved using a **stack**, since:
  - We need to track the most recent opening bracket to match it with a closing one.

### 3️⃣ Plan
1) Initialize an empty stack.
2) Use a dictionary to map closing brackets to their corresponding opening brackets.
3) Iterate through each character in the string:
   - If it’s an opening bracket, push it onto the stack.
   - If it’s a closing bracket, check if it matches the top of the stack:
     - If yes, pop the stack.
     - If no, return False immediately.
4) At the end, if the stack is empty, return True; otherwise, return False.

### 4️⃣ Implementation
see sol.py

### 5️⃣ Complexity Analysis
Assume `N` is the length of the input string:

- **Time Complexity:** `O(N)`  
  - We iterate through the string once and perform `push`/`pop` operations in constant time.
- **Space Complexity:** `O(N)` (worst case)
  - If all characters are opening brackets, they will be stored in the stack.

---

## 6️⃣ Additional Notes
- This problem is a classic **stack-based** problem that often appears in coding interviews.
- If extra characters were allowed in `s`, we would need to ignore them.
- If we needed to **check for missing brackets**, we would need a modified approach.

---

## 📝 Related Problems
- [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
- [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
