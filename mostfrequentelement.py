def get_most_frequent_element(l):
    """
    Given a list, get the element that appears
    with the most frequency. You can assume that 
    there is only one such element, i.e.
    you will not see a list like [2, 2, 1, 1]
    """
    raise NotImplementedError
 
TEST_CASES = [
    # Add more cases here if needed:
     ([1, 2, 3, 1], 1),
     (['hi', 2, 'hi'], 'hi'),
     ([], None),
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
     import sys
     passed_all = True
     for idx,(input_item, expected) in enumerate(test_cases):
        try:
            actual = get_most_frequent_element(input_item)
        except Exception as e:
            print(f'Failed test #{idx + 1} with exception {sys.exc_info()}')
            passed_all = False 
        else:
            if actual != expected:
                print(f'Failed test #{idx + 1}. Input: {input_item}. Actual: {actual}. Expected: {expected}')
                passed_all = False 
     
     if passed_all:
        print('Passed all tests!')
 
 
run_tests(TEST_CASES)