from app.algorithms.branch_and_bound_method import BranchAndBound
from app.algorithms.greedy_search import Greedy
import csv


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


def mainFunc(fileName, nameAlgo):
    w, d, p = choose_data(fileName)
    solution = choose_algo(w, d, p, nameAlgo)
    return solution


# rg = mainFunc(r'C:\Users\Darina\job-sequencing-with-deadline\app\static\task.csv', 'g')
#
# print(rg.greedy_search())
# print(rg.goalFunc)
#
# rb = mainFunc(r'C:\Users\Darina\job-sequencing-with-deadline\app\static\task.csv', 'b')
#
# print(rb.BBM())
# print(rb.lower)




