import numpy as np
import matplotlib.pyplot as plt
import algorithms.result as res

def accuracy_greedy():
    n_greedy = np.array([])
    n_bbm = np.array([])
    goal_greedy = np.array([])
    goal_bbm = np.array([])
    n_greedy1 = np.array([])
    n_bbm1 = np.array([])
    goal_greedy1 = np.array([])
    goal_bbm1 = np.array([])

    for i in range(2, 11):
        for j in range(3):
            w1 = res.makeRandomList(1, 14, i)
            d1 = res.makeRandomList(1, 40, i)
            p1 = res.makeRandomList(1, 20, i)
            w2 = res.makeRandomList(1, 100, i)
            d2 = res.makeRandomList(1, 250, i)
            p2 = res.makeRandomList(1, 200, i)

            gre = res.greedy_analysis_goal(w1, d1, p1)
            gre1 = res.greedy_analysis_goal(w2, d2, p2)

            bbm = res.bbm_analysis_goal(w1, d1, p1)
            bbm1 = res.bbm_analysis_goal(w2, d2, p2)

            goal_greedy = np.append(goal_greedy, gre)
            n_greedy = np.append(n_greedy, i)

            goal_greedy1 = np.append(goal_greedy1, gre1)
            n_greedy1 = np.append(n_greedy1, i)

            goal_bbm = np.append(goal_bbm, bbm)
            n_bbm = np.append(n_bbm, i)

            goal_bbm1 = np.append(goal_bbm1, bbm1)
            n_bbm1 = np.append(n_bbm1, i)

        print(i)
    fig, ax = plt.subplots()

    ax.scatter(n_bbm1, goal_bbm1, color='b', label='МГтаМ з великою різницею тривалостей робіт', s=15)
    ax.scatter(n_bbm, goal_bbm, color='deeppink',
               label='МГтаМ з невеликою різницею тривалостей робіт', s=17)
    ax.scatter(n_greedy, goal_greedy, color='g', label='Жадібний алгоритм з невеликою різницею тривалостей робіт', s=6)
    ax.scatter(n_greedy1, goal_greedy1, color='y',
               label='Жадібний алгоритм з великою різницею тривалостей робіт', s=6)
    ax.legend()
    plt.savefig('plt_accuracy.png')
    plt.show()


accuracy_greedy()