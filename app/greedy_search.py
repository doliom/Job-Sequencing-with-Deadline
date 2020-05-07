def Greedy(w, d, p):
    solution = [] # ініціалізація розкладу
    c = 0 # момент завершення робіт, що вєе у розкладі
    lateness = d # список запізнень для кожної роботи
    goalFunc = 0 # цільова функція
    i = 0
    while(i != len(lateness)):
        currentIndex = lateness.index(min(lateness))
        solution.append(currentIndex + 1)

        print(solution)

        c += p[currentIndex]
        T = max(0, c-d[currentIndex])
        func = func + T*w[currentIndex]
        print(func)

        lateness = list(map(lambda x: x - c, lateness))
        lateness[currentIndex] = 100000
        i = i+1

    return solution