from app.branch_and_bound_method import BranchAndBound
from app.greedy_search import Greedy

def main():
    w = [2, 3, 5, 4, 1, 3, 2]
    d = [1, 4, 3, 8, 4, 6, 2]
    p = [1, 2, 2, 4, 3, 4, 1]
    data_outputG = Greedy(w, d, p)
    greedyResult = data_outputG.greedySearch()

    # print(greedyResult)
    # print(data_outputG.goalFunc)

    data_outputB = BranchAndBound(w, d, p)
    bbmResult = data_outputB.bbm()

if __name__ == "__main__":
    main()