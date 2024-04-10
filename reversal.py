"""
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

"""

# find the words within the string(use the space as separators)
# assign the words to individual string in a list, reverse the position of the word in the list


words = "Eternal sunshine of the spotless mind"
word_list = []
word = ""


for letter in words:
  if letter != " ":
    word += letter
  else:
    word_list.append(word)
    word = ""

word_list.append(word)

# now change their positions
reversed_wordlist = []
for word in word_list:
  reversed_wordlist = [word] + reversed_wordlist

reversed_words = ""
for word in reversed_wordlist:
  reversed_words += " " + word

print("Original words: " + words + "\nReversed words: " + reversed_words)

# Short version
shorter_reversed_wordlist = word_list[::-1]
shorter_reversed_words = " ".join(shorter_reversed_wordlist)
print("Short version reversed words: " + shorter_reversed_words)




    






  



    