from app.branch_and_bound_method import BranchAndBound
from app.greedy_search import Greedy
import csv
from app.charts import draw_chart

def reader_csv():
    with open('individual task.csv', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        buffer = list(reader)
        w = [int(item) for item in buffer[0]]
        d = [int(item) for item in buffer[1]]
        p = [int(item) for item in buffer[2]]
        return w, d, p

def choose_algo(w, d, p):
    print("Choose method: ")
    nameAlgo = input()
    if nameAlgo == 'g':
        data_outputG = Greedy(w, d, p)
        greedyResult = data_outputG.greedy_search()
        print(greedyResult)
        print(data_outputG.goalFunc)
        return greedyResult
    elif nameAlgo == 'b':
        data_outputB = BranchAndBound(w, d, p)
        bbmResult = data_outputB.BBM()
        print(bbmResult)
        return bbmResult


def choose_data():
    print("How you want to give a data: ")
    name = input()
    if name == '0':
        w, d, p = reader_csv()
    else:
        print("soon")
    return w, d, p

def main():
    w, d, p = choose_data()
    solution = choose_algo(w,d, p)
    draw_chart(solution, p)

if __name__ == "__main__":
    main()