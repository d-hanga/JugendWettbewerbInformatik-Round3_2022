from copy import deepcopy

class Biggest:
    @classmethod
    def __go(cls, find, comparisons:list):
        for comparison in comparisons:
            print(f"Alle Vergleiche:        {comparisons}")
            print(f"Alt:                    ***{find}***")
            print(f"Neu:                    ({comparison[0]}, ***{comparison[1]}***)")
            a = "***Nein*** -> ***Nichts Passiert***" if not comparison[1] == find else f"***Ja*** -> ***Neu*** ({comparison}) ***wird zu Alt*** ({find})"
            print(f"Alt Groß =?= Alt Klein? => {a}")
            print()
            if comparison[1] == find:
                return comparison
        return None

    @classmethod
    def __biggest(cls, start, comparisonsoriginal:list):
        comparisons = deepcopy(comparisonsoriginal)
        result = None
        resulttmp = start
        while resulttmp:
            comparisons.remove(resulttmp)
            result = resulttmp[0]
            resulttmp = cls.__go(result, comparisons)
        print("\n\n\n")
        return result

    def __init__(self, *comparisons) -> None:
        self.biggest = Biggest.process(list(comparisons))

    @classmethod
    def process(cls, comparisons:list):
        old = None
        for comparison in comparisons:
            print(f"Alle Vergleiche:        {comparisons}")
            print(f"Start-Vergleich:        {comparison}")
            print()
            new = cls.__biggest(comparison, comparisons)
            if new != old and old != None:
                raise ValueError(f"The biggest can't be told exactly! (According to the calculations it could be: {new, old}, and more uncaclulated ones.)")
            else:
                old = new
        return old
