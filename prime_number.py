'''Check if num is prime or not.'''
import math 

def is_prime(num):
  for i in range(2, int(math.sqrt(num))+1):
    if num%1 == 0:
      return False
  return True


# result = is_prime(33)
# print(result)