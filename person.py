class Person:
  name = []

  def set_name(self,user_name):
    self.name.append(user_name)
    return len(self.name) - 1
  
  def get_name(self,user_id):
    if user_id >= len(self.name):
      return 'There is o such user'
    return self.name[user_id]

if __name__ == '__main__':
  person = Person()
  print('User Bianca has been added with id',person.set_name('Bianca'))
  print('User associated with id 0 is', person.get_name(0))
