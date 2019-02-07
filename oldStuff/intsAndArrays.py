from collections import deque 

def subArraySumToTarget(array, target):
	for i in range (len(array)):
		currSum = 0
		currArray = []	
		for j in range (i, len(array)):
			currSum = currSum + array[j]
			currArray.append(array[j])
			if currSum == target:
				currSum = 0

def threeSum(array, target):
	array.sort()
	for i in range(len(array) - 2):
		a = array[i]
		start = i + 1
		end = len(array) - 1
		while start < end:
			b = array[start]
			c = array[end]
			if a + b + c == target:
				print (a,b,c)
				# continue search for all triplet combinations summing to zero
				if b == array[start + 1]:
					start += 1
				else:
					end -= 1
			elif a + b + c > target:
				end -= 1
			else:
				start += 1

def searchRotatedArray (arr, start, end,target):
	if start > end:
		return -1
	mid = (start+end)//2
	if arr[mid] == target:
		return mid

	if arr[start] <= arr[mid]:
		if target <= arr[mid] and target >= arr[start]:
			return searchRotatedArray(arr, start, mid-1, target)
		else:
			return searchRotatedArray(arr, mid+1, end, target)
	elif arr[mid] < arr[end]:
		if target >= arr[mid] and target <= arr[end]:
			return searchRotatedArray(arr, mid+1, end, target)
		else:
			return searchRotatedArray(arr, start, mid-1, target)

def powers (a, b):
	if b == 0:
		return 1
	else:
		b2 = b/2
		p = powers(a,b2)
		if b % 2 == 0:
			return p*p
		else:
			return p*p*a

# 
def sqrt(x):
    lastGuess= x/2.0
    while True:
        guess = (lastGuess + x/lastGuess)/2
        if abs(guess - lastGuess) < .000001: # example threshold
            return guess
        lastGuess = guess

# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1
# O(n)
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b

# max difference of two elements in the array such that
# larger element appears after the smallest element in the array
# O(n) where n is num elements in arr
def maxDiffInOrder(arr):
	if len(arr) < 2:
		return 0
	maxDiff = arr[1] - arr[0]
	minElement = arr[0]
	for i in range (1,len(arr)):
		if arr[i] > minElement:
			diff = arr[i] - minElement
			if maxDiff < diff:
				maxDiff = diff
		elif arr[i] < minElement:
			minElement = arr[i]
	return maxDiff

# merge two sorted lists
def mergeSortedLists (arr1, arr2):
	returnList = deque()
	q1 = deque (arr1)
	q2 = deque (arr2)
	while a1 and q2:
		if a1[0] > a2[0]:
			returnList.append(a2.popleft())
		else:
			returnList.append(a1.popleft())
	return returnList + q1 + q2

# states if a number is a power of two
# Bitwise AND the number with its just previous number should be equal to ZERO.
def is_power2(num):
	return num != 0 and ((num & (num - 1)) == 0)

# Python program to segregate even and odd elements of array
 
def segregateEvenOdd(arr):
    # Initialize left and right indexes
    left,right = 0,len(arr)-1
    while left < right:
        # Increment left index while we see 0 at left
        while (arr[left]%2==0 and left < right):
            left += 1
        # Decrement right index while we see 1 at right
        while (arr[right]%2 == 1 and left < right):
            right -= 1
        if (left < right):
              # Swap arr[left] and arr[right]*/
              arr[left],arr[right] = arr[right],arr[left]
              left += 1
              right = right-1

def unionFind(lis):
    relationSet = map(set, lis)
    print (relationSet)
    unions = []
    for item in relationSet:
        temp = []
        print (item)
        print (unions)
        for s in unions:
            if not s.isdisjoint(item):
                item = s.union(item)
            else:
                temp.append(s)
        temp.append(item)
        unions = temp
    return unions

# The problem is to count all the possible paths from top left to bottom right of a mXn matrix 
# with the constraints that from each cell you can either move only to right or down
def countNumPaths(n,m):
    # Create a 2D table to store
    # results of subproblems
    count = [[0 for x in range(m)] for y in range(n)]
    # Count of paths to reach any 
    # cell in first column is 1
    for i in range(m):
        count[i][0] = 1;
    # Count of paths to reach any 
    # cell in first column is 1
    for j in range(n):
        count[0][j] = 1;
    # Calculate count of paths for other
    # cells in bottom-up 
    # manner using the recursive solution
    for i in range(1, m):
        for j in range(n):             
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]
# (m-1 + n-1)!/(m-1)!(n-1)!



def main():
	# print (twoSum([7, 4, 10, -6, -2, 13, 2, 0, 17, 9, 6, 15, -4], 13))
	# print (powers(2,8))
	# inputArr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
	# print (searchRotatedArray(inputArr,0,len(inputArr)-1, 6))
	relations = [[1, 2], [2, 3], [4, 5], [6, 7], [1, 7]]
	print (unionFind(relations))

if __name__ == "__main__":
    main()


