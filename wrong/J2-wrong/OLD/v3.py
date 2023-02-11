from time import sleep




def containsonlytuples(l):
    for elem in l:
        if type(elem) != tuple:
            return False
    return True


def toTuple(element:any, stringasiter:bool=False) -> tuple:
    if type(element) == str and stringasiter == False:
        return (element,)
    try:
        return tuple(element)
    except TypeError:
        return (element,)


def chain(weightdifference1:iter, weightdifference2:iter):
    if weightdifference1[-1] == weightdifference2[0]:
        return weightdifference1[:-1] + weightdifference2[1:]
    else:
        return None


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


def secondpart(weightcomparisons):
    pass



# print(firstpart(((4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3))))
print(secondpart(firstpart(((4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3)))))


# print(takeapart(((4,3),2), ((4,3,2),1)))
# print(takeapart(((4,3),2), (1,(4,3,2))))
# print(takeapart(((4,3,2),1), ((4,3),2)))
# print(takeapart((1,(4,3,2)), ((4,3),2)))





4 > 1
3 > 1
4 > 2
3 > 2
4 > 3
2 > 1

(4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3)

4,3,2 > 1
4,3 > 2
4 > 3