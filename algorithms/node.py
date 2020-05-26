class Node:
    def __init__(self, j, w, d, p, parent=None):
        self.__j = j
        self.__w = w
        self.__d = d
        self.__p = p
        self.parent = parent
        self.lower = 0

    @property
    def j(self):
        return [self.__j]

    @j.setter
    def j(self, value):
        if value > 0:
            self.__j = [value]
        elif value == 0:
            self.__j = []
        else:
            raise ValueError

    @property
    def w(self):
        return [self.__w]

    @w.setter
    def w(self, value):
        if value > 0:
            self.__w = [value]
        elif value == 0:
            self.__w = []
        else:
            raise ValueError

    @property
    def d(self):
        return [self.__d]

    @d.setter
    def d(self, value):
        if value > 0:
            self.__d = [value]
        elif value == 0:
            self.__d = []
        else:
            raise ValueError

    @property
    def p(self):
        return [self.__p]

    @p.setter
    def p(self, value):
        if value > 0:
            self.__p = [value]
        elif value == 0:
            self.__p = []
        else:
            raise ValueError
    @property
    def assigned_works(self):
        if self.parent == None:
            return []
        else:
            return self.parent.assigned_works + self.j

    def sum_of_duration(self, JobsIndex, timeList):
        result = 0
        for job in self.freeJobsIndex(JobsIndex):
            result += timeList[job - 1]
        result += self.p[0]
        return result


    def count_lower(self, JobsIndex, timeList):
        if self.parent != None:
            sumOfAllTimes = self.sum_of_duration(JobsIndex, timeList) - self.d[0]
            if sumOfAllTimes < 0:
                Lower = self.parent.lower
            else:
                Lower = sumOfAllTimes * self.w[0] + self.parent.lower
        else:
            Lower = 0
        self.lower = Lower
        return Lower


    def freeJobsIndex(self, JobsIndex):
        return list(set(JobsIndex) - set(self.assigned_works))

    def make_children(self, JobsIndex, weightList, deadlineList, timeList):
        children = []
        for job in self.freeJobsIndex(JobsIndex):
            children.append(Node(job,
                                 weightList[job - 1],
                                 deadlineList[job - 1],
                                 timeList[job - 1],
                                 parent=self))
        return children