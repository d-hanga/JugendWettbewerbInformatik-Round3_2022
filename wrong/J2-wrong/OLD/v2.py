from time import sleep




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


def puttogether(weightdifference1:iter, weightdifference2:iter) -> iter:
    if weightdifference1 == weightdifference2:
        return weightdifference1
    elif weightdifference1[0] == weightdifference2[0]:
        return (weightdifference1[0], toTuple(weightdifference1[1]) + toTuple(weightdifference2[1]))
    elif weightdifference1[1] == weightdifference2[1]:
        return (toTuple(weightdifference1[0]) + toTuple(weightdifference2[0]), weightdifference1[1])
    else:
        return None


def ripapart(weightdifference1:iter, weightdifference2:iter) -> iter:
    new = []
    bigger1 =  weightdifference1[0]
    smaller1 = weightdifference1[1]
    bigger2 =  weightdifference2[0]
    smaller2 = weightdifference2[1]
    if toTuple(bigger1) + toTuple(smaller1) == toTuple(bigger2) or toTuple(smaller1) + toTuple(bigger1) == toTuple(bigger2):
        new.append((bigger1, smaller1))
        new.append((smaller1, smaller2))
    elif toTuple(bigger2) + toTuple(smaller2) == toTuple(bigger1) or toTuple(smaller2) + toTuple(bigger2) == toTuple(bigger1):
        new.append((bigger2, smaller2))
        new.append((smaller2, smaller1))
    elif toTuple(smaller1) + toTuple(bigger1) == toTuple(smaller2) or toTuple(bigger1) + toTuple(smaller1) == toTuple(smaller2):
        new.append((bigger2, bigger1))
        new.append((bigger1, smaller1))
    elif toTuple(smaller2) + toTuple(bigger2) == toTuple(smaller1) or toTuple(bigger2) + toTuple(smaller2) == toTuple(smaller1):
        new.append((bigger1, bigger2))
        new.append((bigger2, smaller2))
    else:
        return None
    return tuple(new)

# 4 > 1
# 3 > 1
# 4 > 2
# 3 > 2
# 4 > 3
# 2 > 1
# def complete(self, weightdifferences):

4,3,2 > 1
4,3 > 2
4 > 3

4 > 1
3 > 1
4 > 2
3 > 2
2 > 1
4 > 3
(5, 4), (4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3)


# first part:
    # going through all the comparisons (c1)
        # going through all the comparisons (c2)
            # calling puttogether on c1 and c2
            # if result isn't None, then
                # add the result ro the results-list

# first part:
    # while loop which only ends when comparisons-list is empty
        # saving the first value of the comparisons (as outside) and removing it from the list
        # while loop which ends when an index (that's set to 0) reaches the end of the list
            #


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




print(firstpart(((4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3))))



# v2
# def firstpart(weightcomparison):
#     weightcomparison = list(weightcomparison)
#     results = []
#     nothingdone = 0
#     i = 0
#     while len(weightcomparison) > 0:
#         outside = weightcomparison.pop(0)
#         j = 0
#         while j < len(weightcomparison):
#             inside = weightcomparison[j]
#             puttogetherresult = puttogether(inside, outside)
#             if puttogetherresult == None:
#                 if nothingdone == 0:
#                     nothingdone = 2
#                 j+=1
#             else:
#                 results.append(puttogetherresult)
#                 weightcomparison.pop(0)
#                 nothingdone = 1
#                 outside = puttogetherresult
#         if nothingdone == 2:
#             results.append(outside)
#             nothingdone = 0
#         nothingdone = 0
#     return results

print(firstpart(((4, 1), (3, 1), (4, 2), (3, 2), (2, 1), (4, 3))))

# second part (repeats until finished -> no tuples inside of the tuples):







# v1
# newweightdifferences = []
# weightdifferences1 = [(4, 1), (3, 1), (4, 2), (3, 2), (4, 3), (2, 1)]
# finished = False
# while len(newweightdifferences) > 0:
#     if len(newweightdifferences) == 0:
#         newweightdifferences.append(weightdifference1[0])
#     weightdifference1 = weightdifferences1.pop(0)
#     i = 0
#     while i < len(weightdifferences1):
#         weightdifference2 = newweightdifferences[i]
#         processputtogether = puttogether(weightdifference2, weightdifference1)
#         print(processputtogether)
#         if processputtogether == None:
#             finished = True
#         else:
#             newweightdifferences.append(processputtogether)
#             finished = False
#         i += 1
# print(newweightdifferences)
