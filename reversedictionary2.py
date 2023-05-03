def reverse_dictionary(dictionary):
    """
    Return a version of the passed-in dictionary for which each:
    * Key is a value from the old dictionary 
    * Value is a list, consisting of the keys in the old dictionary
    
    For example:
        INPUT: {"some_key": "some_value", "some_other_key": "some_value"}
        OUTPUT: {"some_value": ["some_key", "some_other_key"]}
        *sort them out at the beginning instead of creating another loop *

    """
    reversed_dict = {}
    for key, value in dictionary.items():
        if value not in reversed_dict:
            reversed_dict[value] = []
        reversed_dict[value].append(key)
    for value in reversed_dict:
        reversed_dict[value].sort()
    return reversed_dict
 
TEST_CASES = [
 # Add more cases here if needed:
     ({}, {}),
     ({'a': 1}, {1: ['a']}),
     (
         {"some_key": "some_value", "some_other_key": "some_value"},
         {"some_value": ["some_key", "some_other_key"]}
     ),
     (
         {'a': 1, 'b': 1},
         {1: ['a', 'b']}
     ),
     (
         { 'b': 1, 'a': 1, 'c': 1},
         {1: ['a', 'b', 'c']}
     ),
      (
         {'b': 1, 'a': 1, 'c': 'bananas'},
         {1: ['a', 'b'], 'bananas': ['c']}
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