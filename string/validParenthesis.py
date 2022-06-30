class Solution:
    @classmethod
    def isValid(self, s):
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            # Add opening brackets to stack
            if char in dict.values():
                stack.append(char)
            # Check if closing bracket breaks rules
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


test_value = "()[]{}"
result = Solution.isValid(test_value)
print(result)
