from juniorexercise1modified import CheckWords


class Testing:
    @classmethod
    def completetest(cls):
        return cls._vowelgrouptest()+cls._rule1test()+cls._rule2test()+cls._rule3test()+cls._checktest()+cls.checktest()

    def __init__(self):
        self.testingresult = Testing.completetest()
        print(self.testingresult)

    @classmethod
    def _vowelgrouptest(cls,
        WORD = 0,
        SHOULDBE = 1,
        WORDS = (
            ('absorption', 3), ('acceptable', 6), ('acceptance', 6), ('accessible', 6), ('admiration', 5), ('allocation', 5), ('appearance', 6), ('artificial', 5), ('assessment', 3), ('assignment', 3), ('assumption', 3), ('attachment', 3), ('attractive', 7), ('background', 1), ('brainstorm', 2), ('chauvinist', 5), ('collection', 4), ('commitment', 4), ('competence', 6), ('conception', 4), ('conclusion', 5), ('conference', 6), ('confession', 4), ('confidence', 6), ('connection', 4), ('conscience', 5), ('conspiracy', 5), ('constraint', 1), ('continuous', 4), ('conviction', 4), ('correction', 4), ('correspond', 4), ('curriculum', 6), ('definition', 5), ('democratic', 6), ('dependence', 6), ('depression', 4), ('dictionary', 4), ('diplomatic', 6), ('disappoint', 3), ('discipline', 7), ('distribute', 7), ('domination', 5), ('engagement', 5), ('enthusiasm', 4), ('excavation', 5), ('exhibition', 5), ('experiment', 5), ('expression', 4), ('federation', 5), ('foundation', 5), ('girlfriend', 1), ('government', 3), ('hemisphere', 7), ('homosexual', 5), ('houseplant', 4), ('illustrate', 7), ('incredible', 6), ('inhabitant', 5), ('innovation', 5), ('insistence', 6), ('instrument', 5), ('laboratory', 5), ('leadership', 4), ('literature', 7), ('litigation', 5), ('mainstream', 1), ('management', 5), ('mastermind', 4), ('mechanical', 6), ('memorandum', 5), ('occupation', 5), ('perception', 4), ('permission', 4), ('philosophy', 4), ('plagiarize', 7), ('preference', 6), ('presidency', 4), ('prevalence', 6), ('production', 4), ('productive', 7), ('profession', 4), ('provincial', 4), ('psychology', 5), ('reasonable', 6), ('reluctance', 6), ('remunerate', 7), ('repetition', 5), ('reputation', 5), ('researcher', 3), ('resolution', 5), ('separation', 5), ('simplicity', 5), ('stereotype', 4), ('straighten', 3), ('substitute', 7), ('systematic', 6), ('technology', 5), ('vegetation', 5), ('withdrawal', 6)
        )
    ):
        result= "__vowelgroup(str)\n"
        result+="-----------------\n"
        result+="    └> Job: returns the start of the penutlimate vowelgroup of the given string\n\n"
        for wordpack in WORDS:
            shouldbe = wordpack[SHOULDBE]
            word = wordpack[WORD]
            outcome = CheckWords.vowelgroup(word)
            result+=f"    __vowelgroup(\"{word}\")\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
        return result

    @classmethod
    def _rule1test(cls,
        WORD1 = 0,
        WORD2 = 1,
        SHOULDBE = 2,
        WORDS = (
            ('absorption', 'absorption', True), ('absorption', 'brainstorm', False), ('absorption', 'commitment', False), ('absorption', 'depression', False), ('absorption', 'experiment', False), ('absorption', 'foundation', False), ('absorption', 'government', False), ('absorption', 'houseplant', False), ('absorption', 'instrument', False), ('absorption', 'litigation', False), ('brainstorm', 'absorption', False), ('brainstorm', 'brainstorm', True), ('brainstorm', 'commitment', False), ('brainstorm', 'depression', False), ('brainstorm', 'experiment', False), ('brainstorm', 'foundation', False), ('brainstorm', 'government', False), ('brainstorm', 'houseplant', False), ('brainstorm', 'instrument', False), ('brainstorm', 'litigation', False), ('commitment', 'absorption', False), ('commitment', 'brainstorm', False), ('commitment', 'commitment', True), ('commitment', 'depression', False), ('commitment', 'experiment', False), ('commitment', 'foundation', False), ('commitment', 'government', False), ('commitment', 'houseplant', False), ('commitment', 'instrument', False), ('commitment', 'litigation', False), ('depression', 'absorption', False), ('depression', 'brainstorm', False), ('depression', 'commitment', False), ('depression', 'depression', True), ('depression', 'experiment', False), ('depression', 'foundation', False), ('depression', 'government', False), ('depression', 'houseplant', False), ('depression', 'instrument', False), ('depression', 'litigation', False), ('experiment', 'absorption', False), ('experiment', 'brainstorm', False), ('experiment', 'commitment', False), ('experiment', 'depression', False), ('experiment', 'experiment', True), ('experiment', 'foundation', False), ('experiment', 'government', False), ('experiment', 'houseplant', False), ('experiment', 'instrument', False), ('experiment', 'litigation', False), ('foundation', 'absorption', False), ('foundation', 'brainstorm', False), ('foundation', 'commitment', False), ('foundation', 'depression', False), ('foundation', 'experiment', False), ('foundation', 'foundation', True), ('foundation', 'government', False), ('foundation', 'houseplant', False), ('foundation', 'instrument', False), ('foundation', 'litigation', True), ('government', 'absorption', False), ('government', 'brainstorm', False), ('government', 'commitment', False), ('government', 'depression', False), ('government', 'experiment', False), ('government', 'foundation', False), ('government', 'government', True), ('government', 'houseplant', False), ('government', 'instrument', False), ('government', 'litigation', False), ('houseplant', 'absorption', False), ('houseplant', 'brainstorm', False), ('houseplant', 'commitment', False), ('houseplant', 'depression', False), ('houseplant', 'experiment', False), ('houseplant', 'foundation', False), ('houseplant', 'government', False), ('houseplant', 'houseplant', True), ('houseplant', 'instrument', False), ('houseplant', 'litigation', False), ('instrument', 'absorption', False), ('instrument', 'brainstorm', False), ('instrument', 'commitment', False), ('instrument', 'depression', False), ('instrument', 'experiment', False), ('instrument', 'foundation', False), ('instrument', 'government', False), ('instrument', 'houseplant', False), ('instrument', 'instrument', True), ('instrument', 'litigation', False), ('litigation', 'absorption', False), ('litigation', 'brainstorm', False), ('litigation', 'commitment', False), ('litigation', 'depression', False), ('litigation', 'experiment', False), ('litigation', 'foundation', True), ('litigation', 'government', False), ('litigation', 'houseplant', False), ('litigation', 'instrument', False), ('litigation', 'litigation', True)
        )
    ):
        result= "__rule1(str, str, int, int)\n"
        result+="---------------------------\n"
        result+="    └> Job: checks if the two strings match from the penutlimate vowelgroup up to the end\n\n"
        for wordpack in WORDS:
            shouldbe = wordpack[SHOULDBE]
            word1 = wordpack[WORD1]
            word2 = wordpack[WORD2]
            outcome = CheckWords.rule1(word1, word2, CheckWords.vowelgroup(word1), CheckWords.vowelgroup(word2))
            result+=f"    __rule1(\"{word1}\", \"{word2}\", __vowelgroup(\"{word1}\"), __vowelgroup(\"{word2}\"))\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
        return result

    @classmethod
    def _rule2test(cls,
        WORD = 0,
        SHOULDBE = 1,
        WORDS = (
            ('absorption', True), ('acceptable', False), ('acceptance', False), ('accessible', False), ('admiration', True), ('allocation', True), ('appearance', False), ('artificial', True), ('assessment', True), ('assignment', True), ('assumption', True), ('attachment', True), ('attractive', False), ('background', True), ('brainstorm', True), ('chauvinist', True), ('collection', True), ('commitment', True), ('competence', False), ('conception', True), ('conclusion', True), ('conference', False), ('confession', True), ('confidence', False), ('connection', True), ('conscience', True), ('conspiracy', True), ('constraint', True), ('continuous', True), ('conviction', True), ('correction', True), ('correspond', True), ('curriculum', False), ('definition', True), ('democratic', False), ('dependence', False), ('depression', True), ('dictionary', True), ('diplomatic', False), ('disappoint', True), ('discipline', False), ('distribute', False), ('domination', True), ('engagement', True), ('enthusiasm', True), ('excavation', True), ('exhibition', True), ('experiment', True), ('expression', True), ('federation', True), ('foundation', True), ('girlfriend', True), ('government', True), ('hemisphere', False), ('homosexual', True), ('houseplant', True), ('illustrate', False), ('incredible', False), ('inhabitant', True), ('innovation', True), ('insistence', False), ('instrument', True), ('laboratory', True), ('leadership', True), ('literature', False), ('litigation', True), ('mainstream', True), ('management', True), ('mastermind', True), ('mechanical', False), ('memorandum', True), ('occupation', True), ('perception', True), ('permission', True), ('philosophy', True), ('plagiarize', False), ('preference', False), ('presidency', True), ('prevalence', False), ('production', True), ('productive', False), ('profession', True), ('provincial', True), ('psychology', True), ('reasonable', False), ('reluctance', False), ('remunerate', False), ('repetition', True), ('reputation', True), ('researcher', True), ('resolution', True), ('separation', True), ('simplicity', True), ('stereotype', True), ('straighten', True), ('substitute', False), ('systematic', False), ('technology', True), ('vegetation', True), ('withdrawal', False)
        ),
    ):
        result= "__rule2(str, int)\n"
        result+="-----------------\n"
        result+="    └> Job: checks if a string has minimum half its length from the penutlimate vowelgroup up to the end\n\n"
        for wordpack in WORDS:
            shouldbe = wordpack[SHOULDBE]
            word = wordpack[WORD]
            outcome = CheckWords.rule2(word, CheckWords.vowelgroup(word))
            result+=f"    __rule2(\"{word}\", __vowelgroup(\"{word}\"))\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
        return result

    @classmethod
    def _rule3test(cls,
        WORD1 = 0,
        WORD2 = 1,
        SHOULDBE = 2,
        WORDS = (
            ('absorption', 'absorption', False), ('absorption', 'brainstorm', True), ('absorption', 'commitment', True), ('absorption', 'depression', True), ('absorption', 'experiment', True), ('absorption', 'foundation', True), ('absorption', 'government', True), ('absorption', 'houseplant', True), ('absorption', 'instrument', True), ('absorption', 'litigation', True), ('brainstorm', 'absorption', True), ('brainstorm', 'brainstorm', False), ('brainstorm', 'commitment', True), ('brainstorm', 'depression', True), ('brainstorm', 'experiment', True), ('brainstorm', 'foundation', True), ('brainstorm', 'government', True), ('brainstorm', 'houseplant', True), ('brainstorm', 'instrument', True), ('brainstorm', 'litigation', True), ('commitment', 'absorption', True), ('commitment', 'brainstorm', True), ('commitment', 'commitment', False), ('commitment', 'depression', True), ('commitment', 'experiment', True), ('commitment', 'foundation', True), ('commitment', 'government', True), ('commitment', 'houseplant', True), ('commitment', 'instrument', True), ('commitment', 'litigation', True), ('depression', 'absorption', True), ('depression', 'brainstorm', True), ('depression', 'commitment', True), ('depression', 'depression', False), ('depression', 'experiment', True), ('depression', 'foundation', True), ('depression', 'government', True), ('depression', 'houseplant', True), ('depression', 'instrument', True), ('depression', 'litigation', True), ('experiment', 'absorption', True), ('experiment', 'brainstorm', True), ('experiment', 'commitment', True), ('experiment', 'depression', True), ('experiment', 'experiment', False), ('experiment', 'foundation', True), ('experiment', 'government', True), ('experiment', 'houseplant', True), ('experiment', 'instrument', True), ('experiment', 'litigation', True), ('foundation', 'absorption', True), ('foundation', 'brainstorm', True), ('foundation', 'commitment', True), ('foundation', 'depression', True), ('foundation', 'experiment', True), ('foundation', 'foundation', False), ('foundation', 'government', True), ('foundation', 'houseplant', True), ('foundation', 'instrument', True), ('foundation', 'litigation', True), ('government', 'absorption', True), ('government', 'brainstorm', True), ('government', 'commitment', True), ('government', 'depression', True), ('government', 'experiment', True), ('government', 'foundation', True), ('government', 'government', False), ('government', 'houseplant', True), ('government', 'instrument', True), ('government', 'litigation', True), ('houseplant', 'absorption', True), ('houseplant', 'brainstorm', True), ('houseplant', 'commitment', True), ('houseplant', 'depression', True), ('houseplant', 'experiment', True), ('houseplant', 'foundation', True), ('houseplant', 'government', True), ('houseplant', 'houseplant', False), ('houseplant', 'instrument', True), ('houseplant', 'litigation', True), ('instrument', 'absorption', True), ('instrument', 'brainstorm', True), ('instrument', 'commitment', True), ('instrument', 'depression', True), ('instrument', 'experiment', True), ('instrument', 'foundation', True), ('instrument', 'government', True), ('instrument', 'houseplant', True), ('instrument', 'instrument', False), ('instrument', 'litigation', True), ('litigation', 'absorption', True), ('litigation', 'brainstorm', True), ('litigation', 'commitment', True), ('litigation', 'depression', True), ('litigation', 'experiment', True), ('litigation', 'foundation', True), ('litigation', 'government', True), ('litigation', 'houseplant', True), ('litigation', 'instrument', True), ('litigation', 'litigation', False)
        )
    ):
        result= "__rule3(str, str)\n"
        result+="-----------------\n"
        result+="    └> Job: checks if no string is part of the other\n\n"
        for wordpack in WORDS:
            shouldbe = wordpack[SHOULDBE]
            word1 = wordpack[WORD1]
            word2 = wordpack[WORD2]
            outcome = CheckWords.rule3(word1, word2)
            result+=f"    __rule3(\"{word1}\", \"{word2}\")\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
        return result

    @classmethod
    def _checktest(cls,
        WORD1 = 0,
        WORD2 = 1,
        SHOULDBE = 2,
        WORDS = (
            ('absorption', 'absorption', False), ('absorption', 'brainstorm', False), ('absorption', 'commitment', False), ('absorption', 'depression', False), ('absorption', 'experiment', False), ('absorption', 'foundation', False), ('absorption', 'government', False), ('absorption', 'houseplant', False), ('absorption', 'instrument', False), ('absorption', 'litigation', False), ('brainstorm', 'absorption', False), ('brainstorm', 'brainstorm', False), ('brainstorm', 'commitment', False), ('brainstorm', 'depression', False), ('brainstorm', 'experiment', False), ('brainstorm', 'foundation', False), ('brainstorm', 'government', False), ('brainstorm', 'houseplant', False), ('brainstorm', 'instrument', False), ('brainstorm', 'litigation', False), ('commitment', 'absorption', False), ('commitment', 'brainstorm', False), ('commitment', 'commitment', False), ('commitment', 'depression', False), ('commitment', 'experiment', False), ('commitment', 'foundation', False), ('commitment', 'government', False), ('commitment', 'houseplant', False), ('commitment', 'instrument', False), ('commitment', 'litigation', False), ('depression', 'absorption', False), ('depression', 'brainstorm', False), ('depression', 'commitment', False), ('depression', 'depression', False), ('depression', 'experiment', False), ('depression', 'foundation', False), ('depression', 'government', False), ('depression', 'houseplant', False), ('depression', 'instrument', False), ('depression', 'litigation', False), ('experiment', 'absorption', False), ('experiment', 'brainstorm', False), ('experiment', 'commitment', False), ('experiment', 'depression', False), ('experiment', 'experiment', False), ('experiment', 'foundation', False), ('experiment', 'government', False), ('experiment', 'houseplant', False), ('experiment', 'instrument', False), ('experiment', 'litigation', False), ('foundation', 'absorption', False), ('foundation', 'brainstorm', False), ('foundation', 'commitment', False), ('foundation', 'depression', False), ('foundation', 'experiment', False), ('foundation', 'foundation', False), ('foundation', 'government', False), ('foundation', 'houseplant', False), ('foundation', 'instrument', False), ('foundation', 'litigation', True), ('government', 'absorption', False), ('government', 'brainstorm', False), ('government', 'commitment', False), ('government', 'depression', False), ('government', 'experiment', False), ('government', 'foundation', False), ('government', 'government', False), ('government', 'houseplant', False), ('government', 'instrument', False), ('government', 'litigation', False), ('houseplant', 'absorption', False), ('houseplant', 'brainstorm', False), ('houseplant', 'commitment', False), ('houseplant', 'depression', False), ('houseplant', 'experiment', False), ('houseplant', 'foundation', False), ('houseplant', 'government', False), ('houseplant', 'houseplant', False), ('houseplant', 'instrument', False), ('houseplant', 'litigation', False), ('instrument', 'absorption', False), ('instrument', 'brainstorm', False), ('instrument', 'commitment', False), ('instrument', 'depression', False), ('instrument', 'experiment', False), ('instrument', 'foundation', False), ('instrument', 'government', False), ('instrument', 'houseplant', False), ('instrument', 'instrument', False), ('instrument', 'litigation', False), ('litigation', 'absorption', False), ('litigation', 'brainstorm', False), ('litigation', 'commitment', False), ('litigation', 'depression', False), ('litigation', 'experiment', False), ('litigation', 'foundation', True), ('litigation', 'government', False), ('litigation', 'houseplant', False), ('litigation', 'instrument', False), ('litigation', 'litigation', False)
        )
    ):
        result= "__check(str, str, int, int)\n"
        result+="---------------------------\n"
        result+="    └> Job: checks if the two strings are compatible according to the 3 rules\n\n"
        for wordpack in WORDS:
            shouldbe = wordpack[SHOULDBE]
            word1 = wordpack[WORD1]
            word2 = wordpack[WORD2]
            outcome = CheckWords.rule1(word1, word2, CheckWords.vowelgroup(word1), CheckWords.vowelgroup(word2))
            result+=f"    __check(\"{word1}\", \"{word2}\", __vowelgroup(\"{word1}\"), __vowelgroup(\"{word2}\"))\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
        return result

    @classmethod
    def checktest(cls,
        WORDS = 0,
        SHOULDBE = 1,
        WORDSETS = (
            (('absorption', 'assumption', 'conclusion', 'correction', 'discipline', 'foundation', 'insistence', 'memorandum', 'productive', 'resolution'), ()), (('acceptable', 'attachment', 'conference', 'correspond', 'distribute', 'girlfriend', 'instrument', 'occupation', 'profession', 'separation'), (('occupation', 'separation'),)), (('acceptance', 'attractive', 'confession', 'curriculum', 'domination', 'government', 'laboratory', 'perception', 'provincial', 'simplicity'), ()), (('accessible', 'background', 'confidence', 'definition', 'engagement', 'hemisphere', 'leadership', 'permission', 'psychology', 'stereotype'), ()), (('admiration', 'brainstorm', 'connection', 'democratic', 'enthusiasm', 'homosexual', 'literature', 'philosophy', 'reasonable', 'straighten'), ()), (('allocation', 'chauvinist', 'conscience', 'dependence', 'excavation', 'houseplant', 'litigation', 'plagiarize', 'reluctance', 'substitute'), (('allocation', 'excavation'), ('allocation', 'litigation'), ('excavation', 'litigation'))), (('appearance', 'collection', 'conspiracy', 'depression', 'exhibition', 'illustrate', 'mainstream', 'preference', 'remunerate', 'systematic'), ()), (('artificial', 'commitment', 'constraint', 'dictionary', 'experiment', 'incredible', 'management', 'presidency', 'repetition', 'technology'), ()), (('assessment', 'competence', 'continuous', 'diplomatic', 'expression', 'inhabitant', 'mastermind', 'prevalence', 'reputation', 'vegetation'), (('reputation', 'vegetation'),)), (('assignment', 'conception', 'conviction', 'disappoint', 'federation', 'innovation', 'mechanical', 'production', 'researcher', 'withdrawal'), (('federation', 'innovation'),))
        )
    ):
        result= "check(list[str])\n----------------\n    └> Job: checks which strings of a list of strings are compatible according to the 3 rules\n\n"
        for wordset in WORDSETS:
            words = wordset[WORDS]
            shouldbe = wordset[SHOULDBE]
            outcome = CheckWords.check(list(words))
            result+=f"    check(list({words}))\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
        return result
