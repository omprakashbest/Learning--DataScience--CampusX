"""
-> Find Words that can be formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word
in words).

return the sum of lengths of all good strings in words.
"""

from collections import Counter
from collections import defaultdict

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for w in words:
            cur_word = defaultdict(int)
            good = True
            for c in w:
                cur_word[c] += 1
                if c not in count or cur_word[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(w)
        return res
    

obj = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(obj.countCharacters(words, chars))