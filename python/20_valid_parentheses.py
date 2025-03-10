class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[")) # False
    print(s.isValid("()")) # True
    print(s.isValid("()[]{}")) # True
    print(s.isValid("([)]")) # False
            