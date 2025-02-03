# 125. Valid Palindrome

🔗 **[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Two Pointers, String  

---

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.  

Alphanumeric characters include **letters and numbers**.

Given a string `s`, return **true** if it is a palindrome, or **false** otherwise.

---

## Examples

### Example 1:
**Input:**  
```python
s = "A man, a plan, a canal: Panama"
```
**Output:**  
```python
true
```
**Explanation:**  
- After removing non-alphanumeric characters and converting to lowercase, the string becomes `"amanaplanacanalpanama"`.
- This is a palindrome.

### Example 2:
**Input:**  
```python
s = "race a car"
```
**Output:**  
```python
false
```
**Explanation:**  
- After removing spaces and punctuation, the string becomes `"raceacar"`, which is **not** a palindrome.

### Example 3:
**Input:**  
```python
s = " "
```
**Output:**  
```python
true
```
**Explanation:**  
- After removing non-alphanumeric characters, `s` is an empty string `""`, which reads the same forward and backward.

---

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable **ASCII** characters.

---

## 🚀 Solution Approach (UMPIRE Method)

### 1️⃣ Understand
1. What is considered a **palindrome**?  
   - A string that reads the same forward and backward after removing non-alphanumeric characters and ignoring case.
2. How do we handle spaces and punctuation?  
   - Ignore them and only compare **letters and numbers**.
3. Are we allowed to use extra space?  
   - **Optimal approach should use O(1) space**, modifying the input in-place.

### 2️⃣ Match
- This problem involves **string manipulation** and **two pointers**.
- We can use a **left (`l`) and right (`r`) pointer** approach to efficiently compare characters.

### 3️⃣ Plan
1. Use **two pointers**, `l` (left) and `r` (right), initialized at the start and end of `s`.
2. Move `l` forward and `r` backward until both point to **valid alphanumeric characters**.
3. Compare `s[l]` and `s[r]` **case-insensitively**.
4. If they don't match, return **False**.
5. If all valid characters match, return **True**.

---

## 4️⃣ Implementation
see sol.py

## 5️⃣ Complexity Analysis
Assume `N` is the length of `s`.

- **Time Complexity:** `O(N)`  
  - Each character is processed **at most once**.
- **Space Complexity:** `O(1)`  
  - We only use **two pointers** (`l` and `r`).

---

## 6️⃣ Additional Notes
- Using **two pointers** avoids extra memory usage.
- The helper function `alphaNum()` ensures **only alphanumeric characters** are compared.

---

## 📝 Related Problems
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
