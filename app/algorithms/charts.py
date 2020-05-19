import numpy as np
import matplotlib.pyplot as plt

class Chart:
    def __init__(self):
         pass

    def draw_chart(self, jobs, time):
        p = self.sort_time(jobs, time)
        x = np.arange(1)
        sumP = 0
        for i in range(len(p)):
            sumP += i
            plt.barh(x[::-1], p[i], left=np.sum(p[:i], axis=0))
            plt.yticks(x, ["n = 1"])
            plt.xticks(np.arange(0, sumP, 1))
        plt.savefig('plt.png')
        plt.show()


    def sort_time(self, jobs, p):
        sortedP = []
        for i in jobs:
            sortedP.append(p[i-1])
        return sortedP






