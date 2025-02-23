# 409. Longest Palindrome

🔗 **[Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)**  
💡 **Difficulty:** Easy  
🛠 **Topics:** Hash Table, String, Greedy  

---

## Problem Statement

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters.

Letters are **case-sensitive**, meaning `"Aa"` is **not** considered a palindrome.

---

## Examples

### Example 1:
**Input:**  
```python
s = "abccccdd"
```
**Output:**  
```python
7
```
**Explanation:**  
One longest palindrome that can be built is `"dccaccd"`, whose length is `7`.

### Example 2:
**Input:**  
```python
s = "a"
```
**Output:**  
```python
1
```
**Explanation:**  
The longest palindrome that can be built is `"a"`, whose length is `1`.

---

## Constraints
- `1 <= s.length <= 2000`
- `s` consists of **lowercase and/or uppercase** English letters only.

---

## 🚀 Solution Approach (UMPRIME Method)

### 1️⃣ Understand
- We need to **form the longest palindrome** from the given letters.
- **Palindrome Property:**  
  - A palindrome is symmetric, meaning **even frequency characters** can be fully used.
  - **At most one odd frequency character** can be placed at the center.
- **Happy Path Test:**  
  Input: `"abccccdd"` → Output: `7`
- **Edge Cases:**  
  - Single character (e.g., `"a"` → `1`).
  - All characters have even counts (e.g., `"aabbccdd"` → `8`).
  - All characters have odd counts (e.g., `"abc"` → `3`).

---

### 2️⃣ Match
- **Problem Category:** Strings, Hash Tables.
- **Pattern:**  
  - **Greedy Algorithm**:  
    - Use as many even frequency characters as possible.
    - If any character has an odd frequency, allow at most **one** odd character to be used in the center.

---

### 3️⃣ Plan
- **Step 1:** Count the frequency of each character using a hash map.
- **Step 2:** Traverse the frequency map:
  - If a character count is **even**, add its full count to the palindrome length.
  - If a character count is **odd**, add `(count - 1)` to make it even.
  - Track if any odd count exists.
- **Step 3:** If any odd count exists, **add 1** to place one character in the center.

---

### 4️⃣ Implement
see sol.py

---

### 5️⃣ Review
- ✅ **Test with Happy Path:**  
  Input: `"abccccdd"` → Output: `7`
- ✅ **Test with Edge Cases:**  
  - Input: `"a"` → Output: `1`  
  - Input: `"aaa"` → Output: `3`  
  - Input: `"aabbcc"` → Output: `6`  
- ✅ **Checked for Logic Bugs:** Ensured correct palindrome length calculation.
- ✅ **Walked through each iteration step-by-step.**

---

### 6️⃣ Evaluate
- **Time Complexity:** `O(N)`  
  - Counting frequencies and iterating over them is linear.
- **Space Complexity:** `O(1)`  
  - Uses a fixed-size hash map (`26 lowercase + 26 uppercase letters`).

**Pros:**  
- Efficient solution with minimal space usage.
- Simple implementation using a frequency map.

**Cons:**  
- Requires two passes: one for counting, one for constructing the result.

---

### 🔍 Why This Algorithm Works:
- **Key Insight:**  
  - Even frequency characters contribute fully to the palindrome.
  - **At most one** odd frequency character can be placed in the middle.
- **Example Walkthrough:**  
  ```python
  s = "abccccdd"
  freq_map = {"a":1, "b":1, "c":4, "d":2}
  ```
  - Even counts: `4 (c) + 2 (d) = 6`
  - One odd count exists (`a` or `b`), so we add `1`
  - **Final answer: `7`**
  ![alt text](intuition.png)

---

## 📝 Related Problems
- [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) – Check if a string can be rearranged into a palindrome.
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) – Check if a palindrome can be formed by removing at most one character.
