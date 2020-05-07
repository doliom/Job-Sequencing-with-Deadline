from app.branch_and_bound_method import BandBM
from app.greedy_search import Greedy

def main():
    w = [2, 3, 5, 4, 1, 3, 2]
    d = [1, 4, 3, 8, 4, 6, 2]
    p = [1, 2, 2, 4, 3, 4, 1]
    data_output = Greedy(w, d, p)


if __name__ == "__main__":
    main()