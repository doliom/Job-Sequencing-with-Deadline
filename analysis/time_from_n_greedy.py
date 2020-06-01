import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import timedelta
import algorithms.result as res

def task_generation():
    n_greedy = np.array([])
    t_greedy = np.array([])

    for i in range(2, 2001):
        for j in range(3):
            w = res.makeRandomList(1, 10, i)
            d = res.makeRandomList(1, 20, i)
            p = res.makeRandomList(1, 10, i)

            start_time = time.monotonic()
            res.greedy_analysis_time(w, d, p)
            end_time = time.monotonic()
            t = timedelta(seconds=end_time - start_time).microseconds

            t_greedy = np.append(t_greedy, t)
            n_greedy = np.append(n_greedy, i)
        print(i)

    fig, ax = plt.subplots()

    ax.scatter(n_greedy, t_greedy, color='c', label='Жадібний алгоритм', s=6)
    plt.savefig('plt_greedy_t.png')
    plt.show()


task_generation()