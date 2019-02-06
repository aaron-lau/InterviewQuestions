# Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

# Restrictions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def findSmallestIntegerNotInArray(inputArray):
    
    if len(inputArray) < 1:
        return 1
        
    # Move all negative numbers to the left of the array 
    negativeCounter = 0
    for index, number in enumerate(inputArray):
        if number <= 0:
            temp = number
            inputArray[index] = inputArray[negativeCounter]
            inputArray[negativeCounter] = temp
            negativeCounter+=1
    
    positiveArray = inputArray[negativeCounter:]
    if len(positiveArray) < 1:
        return 1
    
    for index, number in enumerate(positiveArray):
        if abs(number) - 1 < len(positiveArray) and positiveArray[abs(number) - 1] > 0:
            positiveArray[abs(number) - 1] = -positiveArray[abs(number) - 1]

    for i in range(len(positiveArray)):
        if positiveArray[i] > 0:
            return i+1

    return len(positiveArray) + 1


