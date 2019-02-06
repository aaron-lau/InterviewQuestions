# An "Array Integer" is an integer represented by an array, where each digit of the integer is an element in the array. 
# For example, the value 123 (one hundred twenty three) would be stored as follows, note the least significant digit is in the zero-th position.

# arrayInt[0] = 3;

# arrayInt[1] = 2;

# arrayInt[2] = 1;

# Implement a method that, given an "ArrayInteger", multiplies another "ArrayInteger". 

# Ex. Given the inputs 123 and 3, the result would be:

# arrayInt[0] = 9;

# arrayInt[1] = 6;

# arrayInt[2] = 3;

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

  
def multArrayInt(array1, array2):
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
  temp_sum = [0] * (len(array1) + len(array2))
  temp_index1 = 0
  temp_index2 = 0
  
  for index1, number1 in enumerate(larger_array):
    carry = 0
    temp_index2 = 0
    
    for index2, number2 in enumerate(smaller_array):
      sum = number1*number2 + temp_sum[temp_index1+temp_index2] + carry
      carry = sum/10
      temp_sum[temp_index1+temp_index2] = sum%10
      temp_index2+=1
    
    if carry:
      temp_sum[temp_index1+temp_index2] += carry
      
    temp_index1+=1
    
  # remove leading 0s
  for number in reversed(temp_sum):
    if len(temp_sum) == 1:
      break
    if number == 0:
      temp_sum.pop()
    else:
      break
  return temp_sum


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
  answer = multArrayInt(array, other)
  printAnswer(answer)
