def get_word_counts(sentence):
    """ Returns a dictionary mapping each word (lowercase) to the number of times 
    it appears in the sentence. Assume no punctuation! """
    
    word_count = {}
    for item in sentence.split():
        if item in word_count:
            word_count[item.lower()] += 1
        else:
            word_count[item.lower()] = 1

    return word_count
        
 
TEST_CASES = [
 # Add more cases here if needed:
     ('', {}),
     (' ', {}),
     ('Cat cat dog cat', {'cat': 3, 'dog': 1}),
     ('Hi Bianca', {'hi': 1, 'bianca': 1})
]

##### IGNORE THE STUFF BELOW THIS LINE 
def run_tests(test_cases):
     import sys
     passed_all = True
     for idx,(l, expected) in enumerate(test_cases):
        try:
            actual = get_word_counts(l)
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