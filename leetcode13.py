# Code for LeetCode Problem #13 – Roman Number Conversion

class Solution:

    def romanToInt(self, s: str) -> int:
        num = 0
        index = len(s) - 1
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while index > 0:

            if d[s[index]] > d[s[index - 1]]:
                num += d[s[index]] - d[s[index-1]]
                index -= 2

            else:
                num += d[s[index]]
                index -= 1

        if index == 0:
            num += d[s[index]]
        return num

print(Solution.romanToInt("IV", "IV")) # Should print 4
print(Solution.romanToInt("LXIV", "LXIV")) # Should print 64
