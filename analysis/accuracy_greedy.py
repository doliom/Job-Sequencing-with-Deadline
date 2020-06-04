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
        for j in range(10):
            w = res.makeRandomList(1, 13, i)
            d = res.makeRandomList(1, 25, i)
            p = res.makeRandomList(1, 11, i)
            gre = res.greedy_analysis_goal(w, d, p)
            bbm = res.bbm_analysis_goal(w, d, p)

            goal_greedy = np.append(goal_greedy, gre)
            n_greedy = np.append(n_greedy, i)

            goal_bbm = np.append(goal_bbm, bbm)
            n_bbm = np.append(n_bbm, i)
            if gre == bbm:
                goal += 1
            count_task += 1
        print(i)
    accuracy = str(goal/count_task*100)
    fig, ax = plt.subplots()
    ax.scatter(n_bbm, goal_bbm, color='g', label='МГтаМ', s=18)
    ax.scatter(n_greedy, goal_greedy, color='deeppink', label='Жадібний алгоритм', s=6)
    ax.legend()
    plt.title("Точність жадібного алгоритму становить  "+accuracy+" %")
    plt.savefig('plt_accuracy.png')
    plt.show()


accuracy_greedy()