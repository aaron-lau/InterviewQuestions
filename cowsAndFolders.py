from collections import deque

# Q: number of cows
# M: shared folders
# N: Confidential folders
# G: Adjacency list

def cowsAndFolders(numCows, m, n, g):
    allFolders = set([item for sublist in g for item in sublist])
    adjacencyList = {}
    sharedFolders = []
    confidentialFolders = []
    membership = {}
    for e1, e2 in g:
        if e1 in adjacencyList:
            adjacencyList[e1].append(e2)
        else:
            adjacencyList[e1] = [e2]
    for folder in m:
        sharedFolders.append(folder[0])
        membership[folder[0]] = folder[1:]
    for folder in n:
        confidentialFolders.append(folder[0])
        membership[folder[0]] = folder[1:]

    # find root node (in degree of 0)
    root = allFolders.copy()
    if len(root) ==  0:
        return " ".join(map (str, set(xrange(numCows))))
    for key, value in adjacencyList.items():
        root -= set(value)
    root = list(root)[0]
    leafs = allFolders - set(adjacencyList.keys())

    q = deque()
    q.append(root)
    while q:
        currNode = q.popleft()
        currNodeMembers = membership[currNode]
        if currNode in leafs:
            continue
        for child in adjacencyList[currNode]:
            if child in sharedFolders:
                membership[child].extend(currNodeMembers)
        q.extend(adjacencyList[currNode])

    coolCows = set(xrange(numCows))
    for folderID, cows in membership.items():
        if folderID in leafs:
            coolCows = coolCows.intersection(set(cows))

    return set(xrange(numCows)) - coolCows

def main():
    Q = 3
    M = [[1, 0],[2, 1]]
    N = [[3,0,1,2]]
    # M = []
    # N = []
    G = []
    # G = [[1,2],[1,3]]
    uncoolCows = cowsAndFolders(Q,M,N,G)
    print (uncoolCows)

if __name__ == "__main__":
    main()
