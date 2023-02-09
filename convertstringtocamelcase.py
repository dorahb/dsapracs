#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them)

def to_camel_case(text):
    #your code here
    if text == '':
        return ''
    else:
        text = text.replace('-', ' ')
        text = text.replace('_', ' ')
        text = text.split()
        for i in range(1, len(text)):
            text[i] = text[i].capitalize()
        return ''.join(text)

print(to_camel_case("the_stealth_warrior"))