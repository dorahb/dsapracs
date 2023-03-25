def get_depth_of_string(l):
    """
    Assume `l` is a list with a single element. That element can either be a string,
    or a list conforming to the same rules as l. Examples of valid lists include:
    []
    [[]]
    [[[]]]
    ['Bianca']
    [['Rye]]
    [[['Sendwave']]]
    This function takes such a list and returns the depth of the 
    string contained therein - or, if there 
    is no such string, None. 
    Please note: One clever way to solve this problem is to cast l to a string and replace
    the square brackets and quotes, e.g. `str(l).replace('[', '').replace(']', '').replace("'", '')`
    For the purpose of this exercise, DO NOT cast l to a string! 
    """
    current_list = l
    depth = 0
    while True:
        if type(current_list) == list:
            if len(current_list)>0:
                current_list = current_list[0]
                depth += 1 
            else:
                return None
        if type(current_list)==str:
            return  depth
        
    """"    for item in l:
        if isinstance(item,str):
            return 1
        elif isinstance(item,list):
            depth = get_depth_of_string(item)
                return depth +1

        """         
            
            
TEST_CASES = [
    # Add more cases here if needed:
    (
      ['hi'],
      1
    ),
    (
      ['hello'],
      1
    ),
    (
      [],
      None
    ),
    (
      [[[['hi']]]],
      4
    )
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = get_depth_of_string(l)
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