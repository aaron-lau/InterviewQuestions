# Given an array of numbers, return every triplet of numbers that can be added up to a given target
# For example, given list A = [12, 3, 4, 1, 6, 9], and target = 24
# The answer should be [(3,9,12)]

# This solution is very similar to the twoElementSum problem 
# but we need an additional loop to compare three numbers together
def threeSum(array,target):
	returnList = []
	for i in range(len(array) - 1):
		# Find pair in subarray array[i+1..n-1] with sum = target - array[i]
		sumMap = {}
		complement = target - array[i]
		for j in range(i+1, len(array)):
			if (complement - array[j]) in sumMap:
				returnList.append([array[i],array[j],complement-array[j]])
			sumMap[array[j]] = j

	return returnList

# print(threeSum([1,1,2,2,3],5))
