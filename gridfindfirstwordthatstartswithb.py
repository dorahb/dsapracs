def find_first_word_that_starts_with_b(grid):
    """ Given a grid represented as a list of lists, returns the first word in the grid 
    that starts with B (lower or uppercase), or None if no such word occurs. 
    """
  
    for word_list in grid:
        for item in word_list:
            if item.lower().startswith('b'):
                return item

            
            
TEST_CASES = [
    # Add more cases here if needed:
    (
      [
        ['dog', 'cat', 'bird'],
        ['fish', 'zebra', 'giraffe']
      ],
      'bird'
    ),
    (
      [
        ['bat', 'cat', 'bird'],
        ['fish', 'zebra', 'giraffe']
      ],
      'bat'
    ),
    (
      [
        ['horse', 'cat', 'elephant'],
        ['fish', 'zebra', 'giraffe']
      ],
      None
    ),
    (
      [
        ['dog', 'cat', 'Bianca'],
        ['fish', 'bird', 'zebra']
      ],
      'Bianca'
    ),
    (
      [],
      None
    ),
    (
      [[], []],
      None
    ),
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
    import sys
    passed_all = True
    for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = find_first_word_that_starts_with_b(l)
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