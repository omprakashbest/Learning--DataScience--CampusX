"""
-> Backspace string compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a 
backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def Compare(string: str):
            res = []
            for ch in string:
                if ch != '#':
                    res.append(ch)
                else:
                    if not res:
                        continue
                    res.pop()
            return res
        return Compare(s) == Compare(t)

# Example    
obj = Solution()
print(obj.backspaceCompare('ab#c', 'ad#c'))