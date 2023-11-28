#check if 5 is in this list 
l = [1,2,3,4,5,6,7,8]

def search(l):
  for item in l:
    if item == 5:
      return True
  return False

t = search(l)
print(t)
