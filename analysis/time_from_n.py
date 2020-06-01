import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import timedelta
import algorithms.result as res


def task_generation():
    n_bbm = np.array([])
    n_greedy = np.array([])
    t_bbm = np.array([])
    t_greedy = np.array([])
    for i in range(2, 101):
        for j in range(10):
            w = res.makeRandomList(1, 10, i)
            d = res.makeRandomList(1, 20, i)
            p = res.makeRandomList(1, 10, i)
            if(i <= 10):
                start_time = time.monotonic()
                res.bbm_analysis_time(w, d, p)
                end_time = time.monotonic()
                t_bbm = np.append(t_bbm, timedelta(milliseconds=end_time - start_time).microseconds)
                n_bbm = np.append(n_bbm, i)

            start_time = time.monotonic()
            res.greedy_analysis_time(w, d, p)
            end_time = time.monotonic()
            t = timedelta(seconds=end_time - start_time).microseconds

            t_greedy = np.append(t_greedy, t)
            n_greedy = np.append(n_greedy, i)


    fig, ax = plt.subplots()

    ax.scatter(n_greedy, t_greedy, color='c', label='Жадібний алгоритм', s=6)
    ax.scatter(n_bbm, t_bbm, color='g', label='МГтаМ', s=12)
    ax.legend()
    plt.savefig('plt.png')
    plt.show()


task_generation()