
from datetime import datetime 

def report_time(other_function, *args, **kwargs):
    start_dt = datetime.now()
    result = other_function(*args, **kwargs)
    time_elapsed = datetime.now() - start_dt
    print(f'Function returned {result} in {time_elapsed}')


def add(a, b):
    return a + b
    

report_time(add, 1, b=2)