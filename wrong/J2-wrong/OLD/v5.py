def finishedsecondpart(l):
    for elem in l:
        if type(elem[0]) == tuple or type(elem[1]) == tuple:
            return False
    return True


def toTuple(element:any, stringasiter:bool=False) -> tuple:
    if type(element) == str and stringasiter == False:
        return (element,)
    try:
        return tuple(element)
    except TypeError:
        return (element,)


def chain(weightdifference:iter):
    l = []
    weightdifference = list(weightdifference)
    while len(weightdifference):
        containerpair = weightdifference[0]
        bigger = containerpair[0]
        smaller = containerpair[1]
        if not len(l):
            l.append(bigger)
            l.append(smaller)
            weightdifference.pop(0)
        else:
            if bigger in l and smaller in l:
                weightdifference.pop(0)
            elif not bigger in l and not smaller in l:
                weightdifference.append(containerpair)
                weightdifference.pop(0)
            else:
                for i in range(len(l)):
                    if l[i] == bigger:
                        l.insert(i + 1, smaller)
                        weightdifference.pop(0)
                        break
                    elif l[i] == smaller:
                        l.insert(i, bigger)
                        weightdifference.pop(0)
                        break
    return l


# def chain2(weightdifference:iter):
#     l = []
#     weightdifference = list(weightdifference)
#     while len(weightdifference):
#         containerpair = weightdifference[0]
#         bigger = containerpair[0]
#         smaller = containerpair[1]
#         if not len(l):
#             l.append(bigger)
#             l.append(smaller)
#             weightdifference.pop(0)
#         else:
#             if bigger in l and smaller in l:
#                 weightdifference.pop(0)
#             elif not bigger in l and not smaller in l:
#                 weightdifference.append(containerpair)
#                 weightdifference.pop(0)
#             else:
#                 if l[-1] == bigger:
#                     l.append(smaller)
#                     weightdifference.pop(0)
#                     break
#                 elif l[0] == smaller:
#                     l.insert(0, bigger)
#                     weightdifference.pop(0)
#                     break
#     return l


def takeapart(weightdifference1:iter, weightdifference2:iter):
    bigger1 =  weightdifference1[0]
    smaller1 = weightdifference1[1]
    bigger2 =  weightdifference2[0]
    smaller2 = weightdifference2[1]

    thisisit = True
    for elem in toTuple(bigger1) + toTuple(smaller1):
        if not elem in toTuple(bigger2):
            thisisit = False
    if thisisit == True:
        return ((bigger1, smaller1), (smaller1, smaller2))

    thisisit = True
    for elem in toTuple(bigger1) + toTuple(smaller1):
        if not elem in toTuple(smaller2):
            thisisit = False
    if thisisit == True:
        return ((bigger2, bigger1), (bigger1, smaller1))

    thisisit = True
    for elem in toTuple(bigger2) + toTuple(smaller2):
        if not elem in toTuple(bigger1):
            thisisit = False
    if thisisit == True:
        return ((bigger2, smaller2), (smaller2, smaller1))

    thisisit = True
    for elem in toTuple(bigger2) + toTuple(smaller2):
        if not elem in toTuple(smaller1):
            thisisit = False
    if thisisit == True:
        return ((bigger1, bigger2), (bigger2, smaller2))


def puttogether(weightdifference1:iter, weightdifference2:iter) -> iter:
    if weightdifference1 == weightdifference2:
        return weightdifference1
    elif weightdifference1[0] == weightdifference2[0]:
        return (weightdifference1[0], toTuple(weightdifference1[1]) + toTuple(weightdifference2[1]))
    elif weightdifference1[1] == weightdifference2[1]:
        return (toTuple(weightdifference1[0]) + toTuple(weightdifference2[0]), weightdifference1[1])
    else:
        return None


def firstpart(weightcomparisons):
    weightcomparisons = list(weightcomparisons)
    results = []
    while len(weightcomparisons) > 0:
        outside = weightcomparisons.pop(0)
        j = 0
        while j < len(weightcomparisons):
            inside = weightcomparisons[j]
            puttogetherresult = puttogether(inside, outside)
            if puttogetherresult == None:
                j+=1
            else:
                weightcomparisons.pop(j)
                outside = puttogetherresult
        results.append(outside)
    return results

def isPure(l):
    for elem in l:
        if type(elem) == tuple:
            return False
    return True

def secondpart(weightcomparisons):
    weightcomparisons = list(weightcomparisons)
    alreadydone = None
    while not finishedsecondpart(weightcomparisons):
        outside = weightcomparisons.pop(0)
        j = 0
        done = False
        while j < len(weightcomparisons):
            inside = weightcomparisons[j]
            takeapartresult = takeapart(inside, outside)
            if takeapartresult == None:
                j+=1
            else:
                weightcomparisons.pop(j)
                weightcomparisons += takeapartresult
                done = True
                break
        if not done and not isPure(outside):
            if alreadydone != outside:
                newoutside = list(outside)
                if type(outside[0]) == tuple:
                    newoutside[0] = outside[0][0]
                if type(outside[1]) == tuple:
                    newoutside[1] = outside[1][0]
            else:
                alreadydone = outside
            weightcomparisons.append(tuple(outside))
    return weightcomparisons








def checkcomparison(bigger, smaller, bigcomparison):
    if bigcomparison.index(bigger) < bigcomparison.index(smaller):
        return True
    return False

def controll(startcomparison, endcomparison):
    for comparison in startcomparison:
        if checkcomparison(comparison[0], comparison[1], endcomparison) == False:
            return False
    return True

b = ((5, 1), (5, 4),(4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3))
print(b)
b = firstpart(b)
print(b)
b = secondpart(b)
print(b)
b = chain(b)
print(b)
print(controll(((4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3)), b))

5 > 1, 4
4, 3, 2 > 1
4, 3 > 2
4 > 3





4 > 1
3 > 1
4 > 2
3 > 2
4 > 3
2 > 1

2 > 1
4 > 3
3 > 2



(4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3)

4,3,2 > 1
4,3 > 2
4 > 3
