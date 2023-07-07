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

LOGS2 = """2023-01-01 15:06 | GET /users | 1000ms
2023-01-01 16:08 | GET /users | 2000ms"""

def extract_endpoints(logs):
    
    split_logs = logs.split('\n')
    all_logs = []

    for line in split_logs:
        split_line = line.split('|')
        split_endpoints = split_line[1]
        all_logs.append(split_endpoints)
    
    return all_logs

# at this point the logs look smt like [{"endpoint": "GET /transactions", "time": 2000}, {"endpoint": "GET /users", "time": 100}]

#(1) Which endpoint is called most frequently?    
def the_most_frequent_endpoint(logs):
    endpoints = extract_endpoints(logs)
    most_frequent_endpoint = get_most_frequent_element(endpoints)
    return most_frequent_endpoint

result = the_most_frequent_endpoint(LOGS)
print(result)

    
# (2) Which endpoint has the longest average (mean) request time?

def extract_endpoint_time(logs):

    split_logs = logs.split('\n')
    all_logs = []
    time_logs = []
    parsed_logs = []

    for line in split_logs:
        split_line = line.split('|')
        split_endpoints = split_line[1]
        split_time = int(split_line[2].strip('ms'))
        parsed_log = {"endpoint":split_endpoints ,"time":split_time}
        all_logs.append(split_endpoints)
        time_logs.append(split_time)
        parsed_logs.append(parsed_log)
    return parsed_logs

# at this point my logs look smt like: [{"endpoint": "GET /transactions", "time": 2000}, {"endpoint": "GET /users", "time": 100}]

def endpoint_with_longest_ave_request_time(logs):
    parsed_logs = extract_endpoint_time(logs)
    no_of_times_endpoints_occurs = {} 
    'lol,such a weird name☝🤣'

    for log in parsed_logs:
        endpoint = log["endpoint"]
        time = log["time"]

        if endpoint in no_of_times_endpoints_occurs:
            no_of_times_endpoints_occurs[endpoint].append(time)
            print(no_of_times_endpoints_occurs)
        else:
            no_of_times_endpoints_occurs[endpoint] = [time]
    
    longest_average_endpoint = max(no_of_times_endpoints_occurs, key=lambda x: sum(no_of_times_endpoints_occurs[x]) / len(no_of_times_endpoints_occurs[x]))
    return longest_average_endpoint

average = endpoint_with_longest_ave_request_time(LOGS)
print(average)

[]
    
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