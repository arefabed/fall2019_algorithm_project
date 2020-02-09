import itertools


class SmartSet():
    def __init__(self, S):
        self.mmbrs = S

    def find_subsets(self):
        self.sbsts = []
        for i in range(1, len(self.mmbrs)):
            l = list(itertools.combinations(self.mmbrs, i))
            for i in l:
                self.sbsts.append(i)

    def find_maximal_subset(self):
        maxlen = 0
        for i in self.sbsts:
            if maxlen < len(i):
                maximal = i
        return maximal

    def remove_set(self, item):
        self.sbsts.remove(item)

    def remove_subsets(self, item):
        self.sbsts = [x for x in self.sbsts if any(i not in item for i in x)]

    def complement(self, item):
        return tuple(x for x in self.mmbrs if x not in item)


if __name__ == "__main__":
    # test
    s = SmartSet({1, 5, 3})
    s.find_subsets()
    mml = s.find_maximal_subset()
    print(s.complement(mml))
    s.remove_subsets((3, 5))
    print(s.sbsts)
    print(s.find_maximal_subset())
