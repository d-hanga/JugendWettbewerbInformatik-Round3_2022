class Container:
    def __lt__(self, other) -> bool:
        if type(other) != type(self):
            raise TypeError(f" '<' not supported between instances of 'Container' and '{type(other)}'")
        return self.weight < other.weight

    def __gt__(self, other) -> bool:
        if type(other) != type(self):
            raise TypeError(f" '>' not supported between instances of 'Container' and '{type(other)}'")
        return self.weight > other.weight

    def __repr__(self) -> str:
        return str(self.weight)

    def __str__(self) -> str:
        return str(self.weight)

    def __init__(self, weight) -> None:
        self.weight = weight





class ContainerManager:
    def __init__(self, *weightdifference:Container):
        self.weightSorted = ContainerManager.checkWeight(*weightdifference)

    @classmethod
    def checkWeight(cls, *weightdifference:Container):
        l = []
        weightdifference = list(weightdifference)
        while len(weightdifference):
            containerpair = weightdifference[0]
            smaller = containerpair[0]
            bigger = containerpair[1]
            if not len(l):
                l.append(smaller)
                l.append(bigger)
                weightdifference.pop(0)
            else:
                if smaller in l and bigger in l:
                    weightdifference.pop(0)
                elif not smaller in l and not bigger in l:
                    weightdifference.append(containerpair)
                    weightdifference.pop(0)
                else:
                    for i in range(len(l)):
                        if l[i] == smaller:
                            l.insert(i + 1, bigger)
                            weightdifference.pop(0)
                        elif l[i] == bigger:
                            print("0001")
                            l.insert(i, smaller)
                            weightdifference.pop(0)
        return l