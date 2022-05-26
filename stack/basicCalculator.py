class Solution:
    @classmethod
    def calculate(self, s: str) -> int:
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in "+(":
                signs.append(signs[-1] * 1)
            if c is "-":
                signs.append(signs[-1] * -1)
            elif c == ")":
                signs.pop()
            i += 1
        return total


Solution.calculate("(1+(4+545+2)-3)+(6+8)")
