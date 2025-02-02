class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } # Mapping close to open brackets

        for c in s: 
            # If c is close, and if the non-empty stack's last element is c's open, then pop it
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # If c is open, append it to the stack
            else:
                stack.append(c)
        # If all opens are popped from the stack, then True, otherwise False
        return True if not stack else False