"""
-> Clear Digits

You are given a string s.
Your task is to remove all digits by doing this operation repreatedly: 
    • Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.
Note: that teh operation cannot be performed on a digit that does not have any non-digit character to its left.
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        del_count = 0

        # Process characters from right to left
        for i in reversed(range(len(s))):
            # If the character is a digit, increment the delete count
            if s[i].isdigit():
                del_count += 1
            elif del_count: # If there are digits to delete, skip the current non-digit character
                del_count -= 1
            else:
                res.append(s[i])
        return "".join(res[::-1])  # Reverse the result to get the correct order

obj = Solution()
s = "cb34"
print(obj.clearDigits(s))