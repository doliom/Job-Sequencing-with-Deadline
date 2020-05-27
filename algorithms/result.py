from algorithms.branch_and_bound_method import BranchAndBound
from algorithms.greedy_search import Greedy
import csv
import random

def reader_csv(fileName):
    with open(fileName, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        buffer = list(reader)
        w = [int(item) for item in buffer[0]]
        d = [int(item) for item in buffer[1]]
        p = [int(item) for item in buffer[2]]
        return w, d, p

def choose_algo(w, d, p, nameAlgo):
    try:
        if nameAlgo == 'g':
            return Greedy(w, d, p)
        elif nameAlgo == 'b':
            return BranchAndBound(w, d, p)
    except ValueError:
        print("uncorrect name of algorithm")

def choose_data(fileName):
    try:
        w, d, p = reader_csv(fileName)
        return w, d, p
    except ValueError:
        print("uncorrect name of file")

def fromFileFunc(fileName):
    w, d, p = choose_data(fileName)
    j = [i for i in range(1, len(w)+1)]
    solutionG = choose_algo(w, d, p, 'g')
    solutionB = choose_algo(w, d, p, 'b')
    return j, w, d , p, solutionG.greedy_search(), solutionB.BBM(), solutionG.goalFunc, solutionB.lower

def makeRandomList(a, b, num):
    list = []
    for i in range(num):
        list.append(random.randint(a, b))
    return list

def randomFunc():
    jobsNum = random.randint(2, 10)

    w = makeRandomList(1, 10, jobsNum)
    d = makeRandomList(1, 20, jobsNum)
    p = makeRandomList(1, 10, jobsNum)

    solutionG = choose_algo(w, d, p, 'g')
    solutionB = choose_algo(w, d, p, 'b')
    j = [i for i in range(1, jobsNum+1)]
    return j, w, d , p, solutionG.greedy_search(), solutionB.BBM(), solutionG.goalFunc, solutionB.lower

def onlineFunc(d_str, w_str, p_str):
    d = list(map(int, d_str.split()))
    w = list(map(int, w_str.split()))
    p = list(map(int, p_str.split()))

    slice = min(len(d), len(w), len(p))
    d = d[:slice]
    w = w[:slice]
    p = p[:slice]

    j = [i for i in range(1, len(w) + 1)]
    solutionG = choose_algo(w, d, p, 'g')
    solutionB = choose_algo(w, d, p, 'b')
    return j, w, d, p, solutionG.greedy_search(), solutionB.BBM(), solutionG.goalFunc, solutionB.lower

# rb = mainFunc(r'C:\Users\Darina\job-sequencing-with-deadline\app\static\task.csv', 'b')





