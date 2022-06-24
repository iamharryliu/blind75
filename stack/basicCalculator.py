class Solution:
    @classmethod
    def calculate(self, s: str) -> int:
        total = 0
        i = 0
        stack = [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                l = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += stack.pop() * int(s[l:i])
                continue
            if c in "+(":
                stack.append(stack[-1])
            if c is "-":
                stack.append(-stack[-1])
            elif c == ")":
                stack.pop()
            i += 1
        return total


Solution.calculate("(1+(4+545+2)-3)+(6+8)")
