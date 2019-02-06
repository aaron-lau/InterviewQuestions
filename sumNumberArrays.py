# An "Array Integer" is an integer represented by an array, where each digit of the integer is an element in the array. 
# For example, the value 123 (one hundred twenty three) would be stored as follows, note the least significant digit is in the zero-th position.

# arrayInt[0] = 3;

# arrayInt[1] = 2;

# arrayInt[2] = 1;

# Implement a method that, given an "ArrayInteger", adds another "ArrayInteger".

# Ex. Given the inputs 123 and 456, the result would be

# arrayInt[0] = 9;

# arrayInt[1] = 7;

# arrayInt[2] = 5;

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

  
def addArrayInt(array1, array2):
  
  # We want the array with less digits be on the  
  # compared to the array with more digits 
  if len(array1) < len(array2):
    larger_array = array2
    smaller_array = array1
  else: 
    larger_array = array1
    smaller_array = array2
    
  # larger_array is guaranteed to be the array with more 
  # or equal number of digits than smaller_array
  larger_array_counter = 0
  smaller_array_counter = 0
  
  carry = 0
  temp_sum = 0
  sum_array = []
  
  # add the smaller array to the larger array
  while smaller_array_counter < len(smaller_array):
    temp_sum = larger_array[larger_array_counter] + smaller_array[smaller_array_counter] + carry
    sum_array.append(temp_sum % 10)
    carry = temp_sum // 10
    
    larger_array_counter+=1
    smaller_array_counter+=1
  
  # if there is any digits that still need to be added in the larger array 
  # add the carry to them
  while larger_array_counter < len(larger_array):
    temp_sum = larger_array[larger_array_counter] + carry
    sum_array.append(temp_sum % 10)
    carry = temp_sum // 10
    
    larger_array_counter+=1
    
  # if there is still a carry, append it to the array (last element)
  if carry:
    sum_array.append(carry)
  
  return sum_array


while (True):
  line = sys.stdin.readline()
  if (len(line) <= 0 or line == '\n'):
    exit()

  array = []
  other = []
  doneFirst = False
  for a in line:
    if (a == '\n'):
      break
    if (a != ';' and not doneFirst):
      array.insert(0, int(a))
      continue
    elif (a == ';'):
      doneFirst = True;
      continue
    other.insert(0, int(a))
  answer = addArrayInt(array, other)
  printAnswer(answer)
