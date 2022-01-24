class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word[1:].islower() and word[0].isupper():
            return True
        if word.islower():
            return True
        return False