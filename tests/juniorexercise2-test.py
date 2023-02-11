from juniorexercise2modified import Biggest



def completetest():
    return gotest() + biggesttest() + processtest()

def gotest(
    FIND = 0,
    COMPARISONS = 1,
    SHOULDBE = 2,
    COMPARISONSSETS = (
        ('c', (('a', 'd'), ('d', 'c'), ('d', 'e'), ('d', 'b'), ('b', 'c'), ('b', 'a'), ('a', 'c'), ('b', 'e'), ('e', 'a'), ('e', 'd')), ('d', 'c')),
        ('b', (('b', 'e'), ('b', 'd'), ('c', 'e'), ('d', 'a'), ('b', 'a'), ('e', 'b'), ('b', 'c'), ('d', 'b'), ('a', 'b'), ('e', 'a')), ('e', 'b')),
        ('e', (('e', 'b'), ('e', 'a'), ('c', 'b'), ('c', 'd'), ('b', 'a'), ('c', 'a'), ('b', 'c'), ('a', 'd'), ('b', 'e'), ('d', 'e')), ('b', 'e')),
        ('d', (('e', 'd'), ('c', 'd'), ('d', 'b'), ('b', 'e'), ('b', 'd'), ('e', 'a'), ('b', 'a'), ('a', 'c'), ('a', 'd'), ('e', 'b')), ('e', 'd')),
        ('e', (('d', 'c'), ('d', 'a'), ('b', 'd'), ('c', 'e'), ('e', 'b'), ('b', 'a'), ('e', 'd'), ('b', 'e'), ('a', 'b'), ('d', 'e')), ('c', 'e')),
        ('d', (('c', 'e'), ('e', 'a'), ('d', 'e'), ('c', 'b'), ('c', 'd'), ('e', 'b'), ('e', 'd'), ('a', 'd'), ('a', 'c'), ('b', 'd')), ('c', 'd')),
        ('e', (('d', 'b'), ('e', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'e'), ('c', 'd'), ('d', 'e'), ('e', 'a'), ('c', 'b'), ('b', 'd')), ('c', 'e')),
        ('a', (('d', 'c'), ('a', 'd'), ('e', 'c'), ('b', 'c'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'd'), ('c', 'b'), ('b', 'd')), ('b', 'a')),
        ('c', (('b', 'e'), ('a', 'e'), ('a', 'd'), ('c', 'e'), ('b', 'c'), ('c', 'a'), ('d', 'a'), ('e', 'c'), ('a', 'b'), ('d', 'b')), ('b', 'c')),
        ('e', (('d', 'a'), ('e', 'c'), ('b', 'a'), ('e', 'd'), ('c', 'b'), ('e', 'a'), ('a', 'e'), ('a', 'c'), ('d', 'b'), ('d', 'c')), ('a', 'e'))
    )
):
    result= "__go(typex, list[array[typex]])\n"
    result+="-------------------------------\n"
    result+="    └> Job: finds the comparison-array with a typex as the smaller one\n\n"
    for comparisonset in COMPARISONSSETS:
        find = comparisonset[FIND]
        comparisons = comparisonset[COMPARISONS]
        shouldbe = comparisonset[SHOULDBE]
        outcome = Biggest.go(find, comparisons)
        if type(find) == str:
            find = "\""+find+"\""
        result+=f"    __go({find}, {comparisons})\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
    return result + "\n"

def biggesttest(
    START = 0,
    COMPARISONS = 1,
    SHOULDBE = 2,
    COMPARISONSSETS = (
        (('e', 'a'), [('a', 'd'), ('d', 'c'), ('d', 'e'), ('d', 'b'), ('b', 'c'), ('b', 'a'), ('a', 'c'), ('b', 'e'), ('e', 'a'), ('e', 'd')], 'b'),
        (('b', 'c'), [('b', 'e'), ('b', 'd'), ('c', 'e'), ('d', 'a'), ('b', 'a'), ('e', 'b'), ('b', 'c'), ('d', 'b'), ('a', 'b'), ('e', 'a')], 'd'),
        (('c', 'd'), [('e', 'b'), ('e', 'a'), ('c', 'b'), ('c', 'd'), ('b', 'a'), ('c', 'a'), ('b', 'c'), ('a', 'd'), ('b', 'e'), ('d', 'e')], 'c'),
        (('e', 'd'), [('e', 'd'), ('c', 'd'), ('d', 'b'), ('b', 'e'), ('b', 'd'), ('e', 'a'), ('b', 'a'), ('a', 'c'), ('a', 'd'), ('e', 'b')], 'e'),
        (('b', 'e'), [('d', 'c'), ('d', 'a'), ('b', 'd'), ('c', 'e'), ('e', 'b'), ('b', 'a'), ('e', 'd'), ('b', 'e'), ('a', 'b'), ('d', 'e')], 'd'),
        (('c', 'b'), [('c', 'e'), ('e', 'a'), ('d', 'e'), ('c', 'b'), ('c', 'd'), ('e', 'b'), ('e', 'd'), ('a', 'd'), ('a', 'c'), ('b', 'd')], 'c'),
        (('a', 'e'), [('d', 'b'), ('e', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'e'), ('c', 'd'), ('d', 'e'), ('e', 'a'), ('c', 'b'), ('b', 'd')], 'c'),
        (('c', 'd'), [('d', 'c'), ('a', 'd'), ('e', 'c'), ('b', 'c'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'd'), ('c', 'b'), ('b', 'd')], 'a'),
        (('d', 'b'), [('b', 'e'), ('a', 'e'), ('a', 'd'), ('c', 'e'), ('b', 'c'), ('c', 'a'), ('d', 'a'), ('e', 'c'), ('a', 'b'), ('d', 'b')], 'd'),
        (('b', 'a'), [('d', 'a'), ('e', 'c'), ('b', 'a'), ('e', 'd'), ('c', 'b'), ('e', 'a'), ('a', 'e'), ('a', 'c'), ('d', 'b'), ('d', 'c')], 'e'))
):
    result= "__biggest(array[typex], list[array[typex]])\n"
    result+="-------------------------------------------\n"
    result+="    └> Job: uses go to find the biggest element (starting with given array)\n\n"
    for comparisonset in COMPARISONSSETS:
        start = comparisonset[START]
        comparisons = comparisonset[COMPARISONS]
        shouldbe = comparisonset[SHOULDBE]
        outcome = Biggest.biggest(start, comparisons)
        result+=f"    __biggest({start}, {comparisons})\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
    return result + "\n"

def processtest(
    COMPARISONS = 0,
    SHOULDBE = 1,
    COMPARISONSSETS = (
        ([('a', 'd'), ('d', 'c'), ('d', 'e'), ('d', 'b'), ('b', 'c'), ('b', 'a'), ('a', 'c'), ('b', 'e'), ('e', 'a'), ('e', 'd')], None),
        ([('b', 'e'), ('b', 'd'), ('c', 'e'), ('d', 'a'), ('b', 'a'), ('e', 'b'), ('b', 'c'), ('d', 'b'), ('a', 'b'), ('e', 'a')],  'd'),
        ([('e', 'b'), ('e', 'a'), ('c', 'b'), ('c', 'd'), ('b', 'a'), ('c', 'a'), ('b', 'c'), ('a', 'd'), ('b', 'e'), ('d', 'e')], None),
        ([('e', 'd'), ('c', 'd'), ('d', 'b'), ('b', 'e'), ('b', 'd'), ('e', 'a'), ('b', 'a'), ('a', 'c'), ('a', 'd'), ('e', 'b')],  'e'),
        ([('d', 'c'), ('d', 'a'), ('b', 'd'), ('c', 'e'), ('e', 'b'), ('b', 'a'), ('e', 'd'), ('b', 'e'), ('a', 'b'), ('d', 'e')], None),
        ([('c', 'e'), ('e', 'a'), ('d', 'e'), ('c', 'b'), ('c', 'd'), ('e', 'b'), ('e', 'd'), ('a', 'd'), ('a', 'c'), ('b', 'd')], None),
        ([('d', 'b'), ('e', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'e'), ('c', 'd'), ('d', 'e'), ('e', 'a'), ('c', 'b'), ('b', 'd')],  'c'),
        ([('d', 'c'), ('a', 'd'), ('e', 'c'), ('b', 'c'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'd'), ('c', 'b'), ('b', 'd')], None),
        ([('b', 'e'), ('a', 'e'), ('a', 'd'), ('c', 'e'), ('b', 'c'), ('c', 'a'), ('d', 'a'), ('e', 'c'), ('a', 'b'), ('d', 'b')], None),
        ([('d', 'a'), ('e', 'c'), ('b', 'a'), ('e', 'd'), ('c', 'b'), ('e', 'a'), ('a', 'e'), ('a', 'c'), ('d', 'b'), ('d', 'c')], None)
    )
):
    result= "__process(array[typex], list[array[typex]])\n"
    result+="-------------------------------------------\n"
    result+="    └> Job: tries every possible start for biggest; if all outcomes are the same, it's the outcomes, else it cannot be defined completly\n\n"
    for comparisonset in COMPARISONSSETS:
        comparisons = comparisonset[COMPARISONS]
        shouldbe = comparisonset[SHOULDBE]
        try:
            outcome = Biggest.process(comparisons)
        except ValueError:
            outcome = None
        result+=f"    process({comparisons})\n        outcome should be: {shouldbe}\n        outcome is:        {outcome}\n        match:             {shouldbe == outcome}\n\n"
    return result + "\n"
