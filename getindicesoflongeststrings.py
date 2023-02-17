def get_indices_of_longest_strings(l):
    """ Returns all indices at which the longest strings in a list appear """
    
    if l == []:
        return []
    
    '''longest_strings = max(len(item) for item in l)
    
    indices = []
    
    for (idx,item) in enumerate(l):
        if len(item) == longest_strings:
            indices.append(idx) '''
    



    indices = []
    
    for (idx,item) in enumerate(l):
        if len(item) == max(len(item)for item in l):
            indices.append(idx)

    return indices
            
            
TEST_CASES = [
    # Add more cases here if needed:
    (['hi', 'hello', 'bye'], [1]),
    (['hi', 'hi', 'I'], [0, 1]),
    (['hi', 'yo', 'I'], [0, 1]),
    ([''], [0]),
    ([], []),
    (['hi', 'yo', 'ye'], [0,1,2])

]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = get_indices_of_longest_strings(l)
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