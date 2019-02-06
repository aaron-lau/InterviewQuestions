# An "Array Integer" is an integer represented by an array, where each digit of the integer is an element in the array. 
# For example, the value 123 (one hundred twenty three) would be stored as follows, note the least significant digit is in the zero-th position.

# arrayInt[0] = 3;

# arrayInt[1] = 2;

# arrayInt[2] = 1;

# Implement a method that, given an "ArrayInteger", increments the value by one.

# Ex. Given the inputs 123, the result would be

# arrayInt[0] = 4;

# arrayInt[1] = 2;

# arrayInt[2] = 1;

import sys

def printAnswer(arrayInt):
  ''' Iterate backwards and print the array, to validate the final product was constructed properly'''
  reverseInt = reversed(arrayInt)
  # MSD should be at the front now.
  # Concatenate all the integer values onto the string and just print it once.
  string_value = ''
  for value in reverseInt:
    string_value += str(value)
  print string_value

  
def incrementArrayInt(arrayInt):
  for index, value in enumerate(arrayInt):
    if value == 9:
      arrayInt[index] = 0
    else: 
      arrayInt[index] += 1
      return arrayInt
  arrayInt.append(1)
      
      
  return arrayInt


while (True):
  line = sys.stdin.readline()
  if (len(line) <= 0 or line == '\n'):
    exit()

  numbers = []
  for a in line:
    if (a == '\n'):
      break
    numbers.insert(0, int(a))
  answer = incrementArrayInt(numbers)
  printAnswer(answer)
