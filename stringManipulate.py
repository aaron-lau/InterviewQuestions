import time

def wordPattern(pattern, input_string, mapping = None):
    if mapping is None: mapping = {}
    if not len(pattern) and not len(input_string): return 1
    for idx, _ in enumerate(input_string):
        sub = input_string[0:idx + 1]
        saved = mapping.get(pattern[0])
        if saved:
            # We are in the call stack that first set the key 
            # and its time to try the next possibility
            if saved[1] == len(pattern):
                mapping[pattern[0]][0] = sub
            # sub does not meet expected string. Could add early return if
            # len(saved[0]) &gt; len(sub)
            if sub != saved[0]: 
            	continue
        else:
            mapping[pattern[0]] = [sub, len(pattern)]

        if wordPattern(pattern[1:], input_string[idx + 1:], mapping):
            return 1
    return 0


def encode(input_string):
    count = 0
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1
    # else:
    entry = (prev,count)
    lst.append(entry)
    return lst
 
 
def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

def lengthOfLongestSubstring(s):
	subString = set([])
	maxLen = 0, windowBack = 0, windowFront = 0
	while (windowBack < len(s) and windowFront < len(s)):
		if s[windowFront] in subString:
			subString.remove([s[windowBack++]])
		else:
			subString[s[windowFront++]]
			maxLen = max(maxLen, windowFront-windowBack)
	return maxLen

def reverseSentence(sentence):
	words = sentence.split()
	reversedSentence = " ".join(reversed(words))
	print reversedSentence


def main():
	break

if __name__ == "__main__":
    main()