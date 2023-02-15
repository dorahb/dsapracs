# Sum the nums, sum the sums and sum the nums up to that sum

def sum_of_sums(nums):
    return sum(sum(nums[:i+1]) for i in range(len(nums)))
print(sum_of_sums([1, 2, 3, 4, 5]))
print(sum_of_sums([1, -2, 3, -4, 5]))
print(sum_of_sums([12, 15, 18, 21, 24]))


