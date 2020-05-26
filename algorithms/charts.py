import numpy as np
import matplotlib.pyplot as plt




def draw_chart(jobs, time):
    p = sort_time(jobs, time)
    x = np.arange(1)
    sumP = 0
    for i in range(len(p)):
        sumP += i
        plt.barh(x[::-1], p[i], left=np.sum(p[:i], axis=0))
        plt.yticks(x, ["n = 1"])
        plt.xticks(np.arange(0, sumP, 1))
    plt.savefig('plt.png')
    # plt.show()


def sort_time(jobs, p):
    sortedP = []
    for i in jobs:
        sortedP.append(p[i-1])
    return sortedP






