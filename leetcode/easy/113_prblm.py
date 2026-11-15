"""
-> Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their respective 
lengths. The length should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

• "s10n" ("s ubstitutio n")
• "sub4u4" ("sub stit u tion")
• "12" ("substitution")
• "su3i1u2on" ("su bst i t u ti on")
• "substitution" (no substrings replaced)

The following are not valid abbreviations:

• "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
• "s010n" (has leading zeros)
• "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1

            elif abbr[j].isalpha() or abbr[j] == '0':
                return False
            else:
                sublen = 0
                while j < len(abbr) and not abbr[j].isalpha():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen
        return i == len(word) and j == len(abbr)

obj = Solution()
word = "internationalization"
abbr = "i12iz4n"
print(obj.validWordAbbreviation(word, abbr))