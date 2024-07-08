# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits: return []

        mapping = {
            '2': list("abc"),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }

        digits = list(digits)

        res = mapping[digits.pop(0)]

        while digits:
            letters = mapping[digits.pop(0)]
            res = [i+j for i in res for j in letters]
            print(res)

        return res