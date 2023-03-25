def flatten_list(l):
    """
    https://www.online-python.com/WC9bP3etGj
    Takes an arbitrarily nested list and returns a flattened version of that list.
    """

""""    flattened_list = []
    current_list = l
   
    while True:
        if type(current_list) == list:
            if len(current_list) > 0:
                current_list = current_list[0]
            else:
                return None
                
        if type(current_list) == str:
            flattened_list.append(current_list)

    return flattened_list """


            
TEST_CASES = [
    # Add more cases here if needed:
    (
      [['Hi'], ['Bianca']],
      ['Hi', 'Bianca']
    ),
    (
      [[[[[]]]], [[]],[]],
      []
    ),
    (
      ['How', 'are', [[[['you'], 'doing']]], [['today']],[], '?'],
      ['How', 'are', 'you', 'doing', 'today', '?']
    ),
    (
      [[[['a',[['b'], [], [[], ['c', [],[[[[['d']]]]]]]]]]], [[]],[]],
      ['a', 'b', 'c', 'd']
    ),
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = flatten_list(l)
        except Exception as e:
            print(f'Failed test #{idx + 1} with exception {sys.exc_info()}')
            passed_all = False 
        else:
            if actual != expected:
                print(f'Failed test #{idx + 1}. List: {l}. Actual: {actual}. Expected: {expected}')
                passed_all = False 
        
    if passed_all:
        print('Passed all tests!')
        
        
run_tests(TEST_CASES)