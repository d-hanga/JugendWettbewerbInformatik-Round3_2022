
while not len(weightdifferences):
    pass
for weightdifference1 in weightdifferences:
    smaller1 = weightdifference1[0]
    bigger1 = weightdifference1[1]
    for weightdifference2 in weightdifferences:
        smaller2 = weightdifference2[0]
        bigger2 = weightdifference2[1]
        if bigger1 + smaller1 == bigger2 or smaller1 + bigger1 == bigger2 :
            pass
        if bigger2 + smaller2 == bigger1 or smaller2 + bigger2 == bigger1 :
            pass
        if smaller1 + bigger1 == bigger2 or bigger1 + smaller1 == bigger2 :
            pass
        if bigger2 + smaller2 == bigger1 or smaller2 + bigger2 == bigger1 :
            pass
        elif smaller1 == smaller2:
            newweightdifferences.append((bigger1 + bigger2, smaller1))
        elif bigger1 == bigger2:
            newweightdifferences.append((bigger1, smaller1 + smaller2))





# 3 > 1
# 4 > 1
# 3 > 2
# 4 > 2
# 4 > 3
# 2 > 1
