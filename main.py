

sample_list = [4,32,1,62,8,53,21,40,39,79,21,22,3,111,25,7]
text = open('SampleText.txt', 'r')


def square_all(lst):
  """Take a list of numbers, square each number, and return the squared list"""

  for idx in range(0, len(lst)):
    lst[idx] = lst[idx] ** 2

  return lst

def sum_all(lst):
  """Take a list, add all its entries, and return the sum"""
  sum = 0
  for num in lst:
    sum += num

  return sum

def reverse_order(lst):
  """Take a list and return a list with entries in the reverse order"""
 
  newList = lst.reverse()


  return lst

def sum_last_3(lst):
  """sum the last 3 entries of the list using the range filter"""
  sum = 0
  for idx in range(len(lst)-3, len(lst)):
    sum += lst[idx]

  return sum

def find_index_of_smallest(lst):
  """find the smallest number in the list, and return its index"""
  index = 0

  smallest_number = 1000000000

  for idx in range(len(lst)):
    if(lst[idx]) < smallest_number:
      smallest_number = lst[idx]
      index = idx

  return index

def find_longest_word(txt):

  """Find the longest word in the text file and return it. """

  lines = list(txt) #store individual lines of text in a list

  all_words = [] #create blank list to eventually add all words too
  for line in lines:
    words = line.split() #split each line into seperate words by blank space, store as list
    all_words.extend(words) #add each word to the list of all words

  
  largest_word = ""
  for w in all_words:
    if(len(w) > len(largest_word)):
      largest_word = w


  return largest_word






#print("The list squared is: " + str(square_all(sample_list)))
#print("The sum of all entries is: " + str(sum_all(sample_list)))
#print("The list in revers order is: " + str(reverse_order(sample_list)))
#print("The sum of the last 3 entries is: " + str(sum_last_3(sample_list)))
#print("The index of the smallest entry is: " + str(find_index_of_smallest(sample_list)))
print("The longest word in the sample text is: " + str(find_longest_word(text)))
