from app.node import Node

class BranchAndBound:
    def __init__(self, w_list, d_list, p_list):
        self.w_list = w_list
        self.d_list = d_list
        self.p_list = p_list
        self.jobs_list = [i for i in range(1, len(w_list)+1)]
        self.lower = 0



    def BBM(self):
        activeSet = []
        Lower = 0 #нижня оцінка
        depth = 0 #глибина вершини з поточною нижньою оцінкою
        currentOpt = 0 #поточний оптимальний розв'язок
        activeSet.append(Node(0, 0, 0, 0))
        while activeSet:
            for node in activeSet:
                activeSet.remove(node)
                for child in node.make_children(self.jobs_list, self.w_list, self.d_list, self.p_list):

                    if Lower == 0:
                        Lower = child.count_lower(self.jobs_list, self.p_list)
                        depth = len(child.assigned_works)
                        activeSet.append(child)
                        currentOpt = child

                    elif Lower < 0:
                        raise ValueError

                    else:
                        if depth == len(child.assigned_works):
                            activeSet.append(child)
                            if child.count_lower(self.jobs_list, self.p_list) < Lower:
                                Lower = child.count_lower(self.jobs_list, self.p_list)
                                currentOpt = child

                        elif len(child.assigned_works) > depth:
                            Lower = child.count_lower(self.jobs_list, self.p_list)
                            currentOpt = child
                            depth = len(child.assigned_works)
                            activeSet.append(child)
                        else:
                            if child.count_lower(self.jobs_list, self.p_list) > Lower:
                                try:
                                    activeSet.remove(child)
                                except ValueError:
                                    continue
                            else:
                                if child.count_lower(self.jobs_list, self.p_list) <= Lower:
                                    activeSet.append(child)
        self.lower = Lower
        return currentOpt.assigned_works