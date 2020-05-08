class BranchAndBound:
    def __init__(self, w, d, p):
        self.w = w
        self.d = d
        self.p = p
        self.lower = 0
        self.jobsIndex = [i for i in range(0, len(w))]

    def bbm(self):
        activeSet = []
        visited = ['']
        currentLower = 0
        self.makeChildren(visited)
        # while activeSet:
        #     for node in activeSet:
        #         print("sdf")


    def makeChildren(self, node):
        children = []
        freeJobsIndex = []
        for i in self.jobsIndex:
            for j in node:
                if i != j:
                    freeJobsIndex.append(i)
                    break
        print(freeJobsIndex)
        # s = []
        # for job in freeJobsIndex:
        #     s = node + [job]
        #     children.append(s)
        #
        # print(children)

        return children