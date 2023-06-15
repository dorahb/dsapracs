def get_most_frequent_element(l):
    """
    Given a list, get the element that appears
    with the most frequency. You can assume that 
    there is only one such element, i.e.
    you will not see a list like [2, 2, 1, 1]
    """

    frequency = {}
    for element in l:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x:x[1])[-1][0]
    
    return sorted_frequency

LOGS = """2023-01-01 12:23 | GET /transactions | 100ms
2023-01-01 15:05 | GET /transactions | 500ms
2023-01-01 15:06 | GET /users | 1000ms
2023-01-01 16:01 | GET /transactions | 100ms
2023-01-01 16:02 | GET /transactions | 105ms
2023-01-01 16:08 | GET /users | 2000ms"""


split_logs = LOGS.split('\n')
all_logs = []


for line in split_logs:
    split_line = line.split('|')
    split_endpoints = split_line[1]
    all_logs.append(split_endpoints)
    
print(all_logs)
    
  
    
  
    




TEST_CASES = [
    # Add more cases here if needed:
     ([1, 2, 3, 1], 1),
     (['hi', 2, 'hi'], 'hi'),
     (['GET /transactions', 'POST /transactions', 'GET /transactions', 'GET /users'],'GET /transactions')
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