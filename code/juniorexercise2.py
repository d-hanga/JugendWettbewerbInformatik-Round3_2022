from copy import deepcopy

class Biggest:
    @classmethod
    def __go(cls, find, comparisons:list):
        for comparison in comparisons:
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
        return result

    def __init__(self, *comparisons) -> None:
        self.biggest = Biggest.process(list(comparisons))

    @classmethod
    def process(cls, comparisons:list):
        old = None
        for comparison in comparisons:
            new = cls.__biggest(comparison, comparisons)
            if new != old and old != None:
                raise ValueError(f"The biggest can't be told exactly! (According to the calculations it could be: {new, old}, and more uncaclulated ones.)")
            else:
                old = new
        return old
