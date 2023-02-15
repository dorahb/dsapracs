def get_indices_of_words_starting_with_b(l):
    """ Returns the indexes of all items startwith with b (or B)"""
    if l == []:
       return []
    
    
    indices = []

    for (idx ,item) in enumerate (l):
        if item.lower().startswith('b'):
            indices.append(idx)
    
    '''    for (idx,item) in enumerate(l):
        if item == '':
            continue
        elif item[0].lower()== 'b':
            indices.append(idx)'''
    
    return indices
        
        
    
            
            
TEST_CASES = [
    # Add more cases here if needed:
    (['bananas', 'dogs', 'boys'], [0, 2]),
    (['Bianca'], [0]),
    ([], []),
    (['alpha', 'beta'],[1]),
    (['baby', 'Bandana', 'balsamic'], [0,1,2]),
    (['Albert','remember','about'],[]),
    (['',],[]),
    (['', 'boy'], [1])
    
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = get_indices_of_words_starting_with_b(l)
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