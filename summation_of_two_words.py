"""
Problem statement:

The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.
"""

class SummationOfTwoWords(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        _alphabets = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9
        }
        fw = sw = tw = ""
        
        for i in range(0, len(firstWord)):
            fw += str(_alphabets[firstWord[i]])

        for j in range(0, len(secondWord)):
            sw += str(_alphabets[secondWord[j]])

        for k in range(0, len(targetWord)):
            tw += str(_alphabets[targetWord[k]])
            
        return True if int(fw) + int(sw) == int(tw) else False
