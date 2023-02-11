bigger1 = ""
bigger2 = ""
smaller1 = ""
smaller2 = ""
new = []
if True:
    if toTuple(bigger1) + toTuple(smaller1) == toTuple(bigger2) or toTuple(smaller1) + toTuple(bigger1) == toTuple(bigger2):
        new.append(bigger1, smaller1)
        new.append(smaller1, smaller2)
    elif toTuple(bigger2) + toTuple(smaller2) == toTuple(bigger1) or toTuple(smaller2) + toTuple(bigger2) == toTuple(bigger1):
        new.append(bigger2, smaller2)
        new.append(smaller2, smaller1)
    elif toTuple(smaller1) + toTuple(bigger1) == toTuple(smaller2) or toTuple(bigger1) + toTuple(smaller1) == toTuple(smaller2):
        new.append(bigger2, bigger1)
        new.append(bigger1, smaller1)
    elif toTuple(smaller2) + toTuple(bigger2) == toTuple(smaller1) or toTuple(bigger2) + toTuple(smaller2) == toTuple(smaller1):
        new.append((bigger1, bigger2))
        new.append((bigger2, smaller2))
