"""
-> Minimum Changes to Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change
any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is 
alternating, While the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

"""

class Solution():
    def miniOperation(self, s: str) -> int:
        count = 0 # operations if s start w 0

        for i in range(len(s)):
            if i % 2: # odd
                count += 1 if s[i] == "0" else 0
            else: # even
                count += 1 if s[i] == "1" else 0

        return min(count, len(s) - count)
    
obj = Solution()
s = "0100"
print(obj.miniOperation(s))