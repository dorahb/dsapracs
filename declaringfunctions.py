# DECLARING A FUNCTION
def get_hello(name):
 return f'Hi, {name}!'
 
def get_goodbye(name):
    return f'Goodbye, {name}!'
    
def print_greetings(names):
    for name in names:
        hello_message = get_hello(name)
        goodbye_message = get_goodbye(name)
        print (f'{hello_message} {goodbye_message}')
        
names = ['Bianca', 'Rye', 'Kamal', 'Jean']
# print_greetings(names)

# def our_greetings():
#     print_greetings(names)
    

    
def say_hi_to_bianca():
    print('Hi, Bianca!')

def add(a, b):
    return a + b
    
# def sumof():
#     result = add(1,2)
#     return result

# hi = our_greetings()


from datetime import datetime

# def report_time(other_function, *args, **kwargs):
#     start_dt = datetime.now()
#     result = other_function(*args, **kwargs)
#     time_elapsed = datetime.now() - start_dt
#     print(f'Function returned {result} in {time_elapsed}')

def report_time(other_function):
    start_time = datetime.now()
    other_function()
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    seconds_elapsed = time_elapsed.total_seconds()
    
    print(f"Total time {time_elapsed} to run.")
  
report_time(lambda :add(1,2))
report_time(lambda :print_greetings(names))



    
    

# CALLING A FUNCTION
# Here, we call `get_greeting`, passing in `Bianca` as the
# first argument. We assign the returned value to the variable
# `result`.
result = get_hello('Bianca')
result2 = get_goodbye('Rye')
# # Print the result, so we can see what it is! 
# print(result,result2)

# TASKS 
# (1) Declare a function `get_goodbye` that takes a name and 
# returns a string saying "goodbye" to that name, e.g. "Goodbye, Bianca!"
#
# (2) Call the function `get_goodbye` (passing in the name "Rye"), and print the result
#
# (3) Declare a function `print_greetings` which takes a list of names and, for each name 
# in the list, prints a string like "Hello, Bianca! Goodbye, Bianca!" This function should
# call both `get_goodbye` and `get_hello`
# 
# (4) Call the function `print_greetings` on the following list of names:
# names = ['Bianca', 'Rye', 'Kamal', 'Jean']
# 
# (5) Declare a function "report_time" which takes another function, runs it, 
# and then prints how long it took to run the function. 
#
# (6) Use your function `report_time` to see how long it takes to run `print_greetings` 
# on the list of names provided above.



