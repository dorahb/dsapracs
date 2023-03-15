def find_longest_strings(grid):
    """ Given a grid represented as a list of lists, returns the first word in the grid 
    that has the longest string, or None if no such word occurs. 
    """
     
    my_list = []

    for word_list in grid:
        for item in word_list:
            my_list.append(item)

    if my_list == []:
        return None
    
    longest_strings = max(my_list, key = len)

    return longest_strings

            
TEST_CASES = [
    # Add more cases here if needed:
    (
      [
        ['dog', 'cat', 'bird'],
        ['fish', 'zebra', 'giraffe']
      ],
      'giraffe'
    ),
    (
      [
        ['bat', 'cat', 'bird'],
        ['fish', 'zebra', 'giraffe']
      ],
      'giraffe'
    ),
    (
      [
        ['horse', 'cat', 'elephant'],
        ['fish', 'zebra', 'giraffe']
      ],
      'elephant'
    ),
    (
      [
        ['dog', 'cat', 'Biancah'],
        ['fish', 'bird', 'zebra']
      ],
      'Biancah'
    ),
    (
        [['dog','cat','bat']
          ],
          'dog'
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
            actual = find_longest_strings(l)
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