def reverse_dictionary(dictionary):
    """ Returns a version of the passed-in dictionary with keys and values 
    swapped. When two values for the output dictionary conflict, prefer the 
    one that comes first numerically/alphabetically."""
    
    reversed_dictionary = {}

    for key,value in dictionary.items():
        if value in reversed_dictionary:
            if reversed_dictionary[value]<key:
                key = reversed_dictionary[value]

        reversed_dictionary[value] = key

    return reversed_dictionary
 
TEST_CASES = [
 # Add more cases here if needed:
     ({}, {}),
     ({'a': 1}, {1: 'a'}),
     (
         {'a': 1, 'b': 1},
         {1: 'a'}
     ),
     (
         { 'b': 1, 'a': 1, 'c': 1},
         {1: 'a'}
     ),
      (
         {'b': 1, 'a': 1, 'c': 'bananas'},
         {1: 'a', 'bananas': 'c'}
     )    
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
     import sys
     passed_all = True
     for idx,(input_dict, expected) in enumerate(test_cases):
        try:
            actual = reverse_dictionary(input_dict)
        except Exception as e:
            print(f'Failed test #{idx + 1} with exception {sys.exc_info()}')
            passed_all = False 
        else:
            if actual != expected:
                print(f'Failed test #{idx + 1}. Input: {input_dict}. Actual: {actual}. Expected: {expected}')
                passed_all = False 
     
     if passed_all:
        print('Passed all tests!')
 
 
run_tests(TEST_CASES)