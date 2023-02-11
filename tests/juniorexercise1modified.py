from copy import deepcopy

class CheckWords:
    vowels = ("aeiou")

    @classmethod
    def vowelgroup(cls, word:str) -> int:
        if len(word) == 0:
            raise ValueError("Not Enough Letters: No letters in word!")
        lastvowel = None
        if word[len(word)-1] in cls.vowels:
            lastvowel = len(word)-1
        i = len(word)-2
        while i > -1:
            if word[i] in cls.vowels:
                if not word[i+1] in cls.vowels and lastvowel != None:
                    while i > 0 and word[i-1] in cls.vowels:
                        i-=1
                    return i
                lastvowel = i
            i-=1
        return lastvowel

    @classmethod
    def rule1(cls, word1: str, word2: str, vowelgroupforword1:int, vowelgroupforword2:int) -> bool:
        return word1[vowelgroupforword1:len(word1)] == word2[vowelgroupforword2:len(word2)]

    @classmethod
    def rule2(cls, word: str, vowelgroup:int) -> bool:
        return len(word[vowelgroup:len(word)]) >= len(word)/2

    @classmethod
    def rule3(cls, word1: str, word2: str) -> bool:
        return not word1 in word2 and not word2 in word1

    @classmethod
    def check_(cls, word1:str, word2:str, vowelgroupforword1:int, vowelgroupforword2:int) -> bool:
        return cls.rule1(word1, word2, vowelgroupforword1, vowelgroupforword2) and cls.rule2(word1, vowelgroupforword1) and cls.rule2(word2, vowelgroupforword2) and cls.rule3(word1, word2)

    def __init__(self, *words) -> None:
        self.state = CheckWords.check(list(words))

    @classmethod
    def check(cls, wordsoriginal:list[str]) -> tuple:
        words = deepcopy(wordsoriginal)
        correctconnections = []
        if len(words) < 2:
            raise ValueError(f"Not Enough Words: There must be at least two words. You have {len(words)} words.")
        while len(words) > 1:
            word1 = words.pop(0).lower()
            vowelgroupforword1 = cls.vowelgroup(word1)
            j = 0
            while j < len(words):
                word2 = words[j].lower()
                vowelgroupforword2 = cls.vowelgroup(word2)
                if cls.check_(word1, word2, vowelgroupforword1, vowelgroupforword2):
                    correctconnections.append((word1, word2))
                j+=1
        return tuple(correctconnections)
