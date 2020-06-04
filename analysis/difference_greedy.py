import numpy as np
import matplotlib.pyplot as plt
import algorithms.result as res

def difference_greedy():
    dif = np.array([])
    n_greedy = np.array([])
    n_bbm = np.array([])
    goal_greedy = np.array([])
    goal_bbm = np.array([])


    for i in range(2, 11):
        w = res.makeRandomList(1, 13, i)
        d = res.makeRandomList(1, 25, i)
        p = res.makeRandomList(1, 11, i)
        gre = res.greedy_analysis_goal(w, d, p)
        bbm = res.bbm_analysis_goal(w, d, p)
        if bbm != 0:
            buffer = abs(gre/bbm - 1)*100
        else:
            buffer = gre*100
        dif = np.append(dif, buffer)

        goal_greedy = np.append(goal_greedy, gre)
        n_greedy = np.append(n_greedy, i)

        goal_bbm = np.append(goal_bbm, bbm)
        n_bbm = np.append(n_bbm, i)

        print(i)

    difference = str(np.mean(dif))
    fig, ax = plt.subplots()
    plt.plot(n_bbm, goal_bbm, color='g', label='МГтаМ')
    plt.plot(n_greedy, goal_greedy, color='deeppink', label='Жадібний алгоритм')
    plt.legend()
    plt.savefig('plt_diff.png')
    plt.show()
    print("Відсоток відхилення від opt для жадібного алгоритму становить  ", difference, "%")


difference_greedy()