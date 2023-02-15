def get_indices_of_largest_item(l):
    """ Returns all indices at which the largest item in a list of items appears """
    if l == []:
       return []
       
   
    """   largest_item = l[0]

   for item in l:
        if item > largest_item:
            largest_item = item

    indices = []
             
               for (idx,item) in enumerate(l):
        if item == largest_item:
            indices.append(idx)

            return indices
            
            """


    largest_item = max(l)
    indices = []
    
    for (idx,largest_item) in enumerate(l):
        if largest_item == max(l):
            indices.append(idx)
    
    return indices






            
            
TEST_CASES = [
    # Add more cases here if needed:
    ([1, 3, 2], [1]),
    ([3, 1, 3], [0, 2]),
    ([], []),
    ([3,3,3],[0,1,2]),
    ([-3,-2,-1],[2]),
    ([-5,0],[1])

    
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = get_indices_of_largest_item(l)
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

