#find the sum of the minimum values in each row


def sum_of_minimums(numbers):

    return sum(min(i) for i in numbers)

print(sum_of_minimums([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]]))

 


