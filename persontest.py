import unittest



# This is the class we want to test. So, we need to import it
from person import Person as PersonClass

class Test(unittest.TestCase):
  person = PersonClass.Person()# instantiate the Person Class
  user_id = [] #stores obtained user_id
  user_name = [] #stores obtained user_name

  # test case function to check the Person.set_name function

  def test_set_name(self):
    print("Start set name test")

    for i in range(4):
      name = 'name' + str(i) #initialize a name
      self.user_name.append(name) #add the name to the list variable above
      user_id = self.person.set_name(name) #get user id 
      self.assertIsNotNone(user_id) #confirm if id null or not, null will fail test
      self.user_id.append(user_id)#add the id to the list variable above

    print('user_id length=', len(self.user_id))
    print(self.user_id)
    print('user_name length=', len(self.user_name))
    print(self.user_name)
    print("\nFinish set_name test\n")

  

