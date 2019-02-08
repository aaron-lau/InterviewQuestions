# Determine if a string be decomposed into a list of substrings, 
# s.t. every substring is one of the elemnts of the set of words.

def wordBreak(string, subset):
    # true when string can be cut off successfully at 0 - (i-1)
    canBeCutOff = [False] * (len(string) + 1)
    canBeCutOff[0] = True

    # O(len(string) * len(words))
    for i in range(0,len(string)):
        if not canBeCutOff[i]:
            continue
    
        for word in subset:
            if i + len(word) > len(string):
                continue

            if string[i:i + len(word)] == word:
                canBeCutOff[i + len(word)] = True

    return canBeCutOff[-1]

# print(wordBreak("amanabreak", ["a", "man", "break"]))
# print(wordBreak("amanabreak", ["break"]))
# print(wordBreak("abcd", ["ab", "abc", "d"]))
