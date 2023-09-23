# Today, we learned about the * operator, which in a function signature 
# can be used to refer to an arbitrary number of positional arguments:

def count_positional_arguments(*args):
    print(f'Caller passed in {len(args)} positional arguments: {args}')
    
count_positional_arguments('a', 'b', 'c')

# We also learned about the ** operator, which in a function signature
# can be used to refer to an arbitrary number of keyword arguments:
def count_keyword_arguments(**kwargs):
    print(f'Caller passed in {len(kwargs)} keyword arguments: {kwargs}')
    
count_keyword_arguments(first='a', second='b', third='c')

# TASK 1:
# Consider the following code snippet. Before running it, write down 
# the expected output. Then run the code and check your work!
def print_values(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_values(1, 2, 3, a=4, b=5)


# TASK 2:
# Write a function combine_lists_and_dict that takes
# multiple arguments: a list of items, a dictionary of items,
# and a variable number of additional positional and keyword arguments.
# The function should combine all the input items into a single list and return it.

def combine_lists_and_dict(*args, **kwargs): # NOTE: please update type signature as needed
    combined_list = []
    
    for arg in args:
        # print(arg)
        if isinstance(arg,list):
            combined_list.extend(arg)
            # print(combined_list)
        elif isinstance(arg,dict):
            combined_list.extend(arg.values())
            # print(combined_list)
        else:
            combined_list.append(arg)
            # print(combined_list)
            
    combined_list.extend(kwargs.values())
    # print(combined_list)
    return combined_list
    
    
    
result = combine_lists_and_dict(['apple', 'banana'], {'color': 'yellow'}, 'cherry', shape='round')
assert result == ['apple', 'banana', 'yellow', 'cherry', 'round'], f'Unexpected result: {result}'

# TASK 3:
# Let's say we only want to call functions on behalf of a specific 
# set of users (ALLOWED_USERS). Implement `run_function_if_allowed` 
# such that:
# (1) If `current_user` does not belong to `ALLOWED_USERS`, it raises 
# an exception
# (2) If `current_user` does belong to `ALLOWED_USERS`, it runs the function
# with the passed-in arguments, and returns the result

ALLOWED_USERS = ['rye', 'bianca']

def run_function_if_allowed(current_user, func, *args, **kwargs):
    if current_user in ALLOWED_USERS:
        return func(*args,**kwargs)
    else:
        raise Exception(f"{current_user} is not allowed to run this function")

# Here's some code to make sure your solution works! 

def get_bio(name, age):
    return f'{name} is {age} years old'
    
result = run_function_if_allowed('bianca', get_bio, 'Lina', age=55)
assert result == 'Lina is 55 years old', f'Unexpected result: {result}'

try:
    result = run_function_if_allowed('someone-else', get_bio, 'Lina', age=55)
except Exception:
    pass 
else:
    print('Oops, should have raised exception!')



