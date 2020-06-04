import numpy as np
import matplotlib.pyplot as plt
import algorithms.result as res


def accuracy_greedy():
    n_greedy = np.array([])
    n_bbm = np.array([])
    goal_greedy = np.array([])
    goal_bbm = np.array([])
    goal = 0
    count_task = 0
    for i in range(2, 11):
        for j in range(3):
            w1 = res.makeRandomList(1, 14, i)
            d1 = res.makeRandomList(1, 40, i)
            p1 = res.makeRandomList(1, 20, i)
            w2 = res.makeRandomList(1, 100, i)
            d2 = res.makeRandomList(1, 250, i)
            p2 = res.makeRandomList(1, 200, i)
            gre = res.bbm_analysis_goal(w1, d1, p1)
            bbm = res.bbm_analysis_goal(w2, d2, p2)

            goal_greedy = np.append(goal_greedy, gre)
            n_greedy = np.append(n_greedy, i)

            goal_bbm = np.append(goal_bbm, bbm)
            n_bbm = np.append(n_bbm, i)

        print(i)
    fig, ax = plt.subplots()
    ax.scatter(n_bbm, goal_bbm, color='g', label='МГтаМ з великою різницею тривалостей робіт', s=18)
    ax.scatter(n_greedy, goal_greedy, color='deeppink',
               label='ЖМГтаМ з невеликою різницею тривалостей робіт', s=6)
    ax.legend()
    plt.savefig('plt_data_bbm.png')
    plt.show()


accuracy_greedy()