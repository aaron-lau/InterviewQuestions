# Given an array of numbers, return every pair of numbers that can be added up to a given target
# For example, given list A = [5, -2, 4, 9, 1], and target = 6
# The answer should be [(5,1)]


def twoSum(array, target):
	# create a hash map where the key an element of the input array
	# and the value is the index of that element in the input array (that it was last seen)
	# The value is optional and purely to return the index of the elements that sum to target if necessary
	sumMap = {}
	returnList = []

	for i in range(len(array)):
		complement = target - array[i]
		# We see the (target - array[i]) is in our hashmap 
		# If it has, than we have a sum 
		if complement in sumMap:
			returnList.append((complement, array[i]))
		# now that we have seen an element update it's last seen index 
		sumMap[array[i]]= i

	return returnList

# print(twoSum([], 0))
# print(twoSum([1,2,3,4,-5], -4))
# print(twoSum([5, -2, 4, 9, 1], 6))
# print(twoSum([5, 5], 10))
