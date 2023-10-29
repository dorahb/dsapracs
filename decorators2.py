#write a decorator that (1) runs the function if today is a weekend (use GMT timezone) 
# (2) raises an error if today is not a weekend


# today = datetime.now().strftime('%A')
# print(today)
    

"""https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday, https://pypi.org/project/pytz/ """

from datetime import datetime
from pytz import timezone 

def weekend_only(func):
    def weekend_func(*args, **kwargs):
        gmt = timezone('GMT') 
        today = datetime.now(gmt).strftime('%A') 
        if today in ['Saturday', 'Sunday']:
            print(today)
            return func(*args, **kwargs)
        else:
            raise ValueError("Function can only be run on weekends (Saturday or Sunday) in GMT timezone.")

    return weekend_func

@weekend_only
def the_weekend(day):
    print(f'Today is {day}')

the_weekend(day="Friday") 
