from app.algorithms.branch_and_bound_method import BranchAndBound
from app.algorithms.greedy_search import Greedy
import csv

class Result:
    def __init__(self):
        pass

    def reader_csv(self, fileName):
        with open(fileName, newline='') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            buffer = list(reader)
            w = [int(item) for item in buffer[0]]
            d = [int(item) for item in buffer[1]]
            p = [int(item) for item in buffer[2]]
            return w, d, p

    def choose_algo(self, w, d, p, nameAlgo):
        try:
            if nameAlgo == 'g':
                return Greedy(w, d, p)
            elif nameAlgo == 'b':
                return BranchAndBound(w, d, p)
        except ValueError:
            print("uncorrect name of algorithm")


    def choose_data(self, fileName):
        try:
            if fileName == 'example':
                w, d, p = self.reader_csv('individual task.csv')
            elif fileName == 'count':
                w, d, p = self.reader_csv(fileName)
            return w, d, p
        except ValueError:
            print("uncorrect name of file")


    def main(self, fileName, nameAlgo):
        w, d, p = self.choose_data(fileName)
        solution = self.choose_algo(w, d, p, nameAlgo)
        return solution
        #
        # graf = Chart()
        # graf.draw_chart(solution, p)