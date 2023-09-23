from time import sleep 
from datetime import datetime

def timed(func):
    def altered_func(*args, **kwargs):
        start_dt = datetime.now()
        return_value = func(*args, **kwargs)
        end_dt = datetime.now()
        # Print how long it took to run the function
        print(f'It took {end_dt - start_dt}')
        return return_value
    
    return altered_func
    

@timed
def say_hello(name):
    print(f'Hello {name}!')

@timed
def slow_say_hello():
    sleep(2)
    print('Hello')



say_hello(name='Bianca')
slow_say_hello()