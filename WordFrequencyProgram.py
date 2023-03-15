'''Create a program that takes a string as input and returns the most common word in the string along with its frequency. If there is a tie, return the word that appears first in the string.

For example, if the input string is "the quick brown fox jumps over the lazy dog", the program should return "the" and its frequency of 2, since "the" appears twice in the string.

Here are some additional requirements:

The program should be case-insensitive, so "The" and "the" should be considered the same word.
The program should ignore punctuation marks, so "fox," and "fox" should be considered the same word.
The program should return a tuple containing the most common word and its frequency.
If the input string is empty, the program should return None.'''

def most_common_word(text):
    if not text:
        return None
    
    words = text.lower().split()
    
    # Count the frequencies of each word using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Find the most common word and its frequency
    most_common_word = max(word_counts, key=word_counts.get)
    frequency = word_counts[most_common_word]
    
    return (most_common_word, frequency)
