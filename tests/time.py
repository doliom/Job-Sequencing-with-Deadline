import time
from algorithms.result import *

def my_timer(f):
    def tmp(*args, **kwargs):
        start_time=time.time()
        result=f(*args, **kwargs)
        delta_time=time.time() - start_time
        print('Время выполнения функции {}' .format(delta_time))
        return result

    return tmp

@my_timer
def my_sum():
    # rаb = mainFunc(r'C:\Users\Darina\job-sequencing-with-deadline\app\static\individual_task_100.csv', 'b')
    #
    # print(rаb.BBM())
    # print(rаb.lower)
    sg = fromFileFunc(r'C:\Users\Darina\job-sequencing-with-deadline\static\csv\individual_task_100.csv')
    print(sg.greedy_search())
    print(sg.goalFunc)

    print(sg.BBM())
    print(sg.Lower)

print (my_sum())