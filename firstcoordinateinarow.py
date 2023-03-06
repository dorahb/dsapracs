def find_x(rows):
    """ Returns the first coordinate at which the string 'X' occurs, or None if the string 
    'X' does not occur. 
    
    Coordinates are represented as a tuple, e.g.:
    * (0, 0) means first row, first column
       [
          ['X', 'O'],
          ['O', 'O']
       ]
    * (1, 0) means second row, first column
        [
          ['O', 'O'],
          ['X', 'O']
        ]
    * (0, 1) means first row, second column 
        [
          ['O', 'X'],
          ['O', 'O']
        ]
    
    """
    for (index,row) in enumerate(rows):
        for (idx,item) in enumerate(row):
                if item == 'X': 
                    return index,idx

            
            
TEST_CASES = [
    # Add more cases here if needed:
    (
      [
        ['O', 'O', 'X'],
        ['O', 'O', 'O']
      ],
      (0, 2)
    ),
    (
      [
        ['O', 'O', 'O'],
        ['X', 'O', 'O']
      ],
      (1, 0)
    ),
    (
      [
        ['O', 'O', 'X'],
        ['X', 'O', 'O']
      ],
      (0, 2)
    ),
    (
      [
        ['O', 'O', 'O'],
        ['O', 'O', 'O']
      ],
      None
    ),
    (
      [],
      None
    ),
    (
      [[], []],
      None
    ),
    (
      [
          [],
          ['O', 'X']
      ],
      (1, 1)
    ),
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = find_x(l)
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