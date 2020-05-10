class Greedy:
    def __init__(self, w, d, p):
        self.w = w
        self.d = d
        self.p = p
        self.lateness = d
        self.goalFunc = 0
        self.c = 0 #запізнення

    def greedy_search(self):
        i = 0
        solution = []
        while (i != len(self.lateness)):
            currentIndex = self.lateness.index(min(self.lateness))
            solution.append(currentIndex + 1)
            self.c += self.p[currentIndex]
            self.take_goal_func(currentIndex)
            self.lateness = list(map(lambda x: x - self.c, self.lateness))
            self.lateness[currentIndex] = 100000
            i = i + 1
        return solution

    def take_goal_func(self, currentIndex):
        T = max(0, self.c - self.d[currentIndex])
        self.goalFunc = self.goalFunc + T * self.w[currentIndex]

