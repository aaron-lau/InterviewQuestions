class dfsClass:
	def dfs (self, graph):
		for vertex in graph:
			self.colour[vertex] = white
			self.predecssor[vertex] = null
		self.time = 0
		for vertex in graph:
			if colour[vertex] == white:
				self.DFSvisit(v)

	def DFSvisit(self, v):
		self.colour[v] = gray
		self.time += 1
		for neighbor in v.neighbors:
			if self.colour[v] == white:
				self.predecssor[neighbor] = v
				self.DFSvisit(neighbor)
		self.colour[v] = black

def bfs (source):
	q = queue.Queue()
	root.visited = true
	q.put (root)
	while not q.empty():
		nextNode = queue.get()
		for neighbor in root.adjacentList:
			if neighbor.visited == false:
				neighbor.visited = true

class Trie(object):
    def __init__(self):
        self.children = {}
        self.flag = False # Flag to represent that a word ends at this node

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.flag = True

    def all_suffixes(self, prefix):
        results = set()
        if self.flag:
            results.add(prefix)
        if not self.children: 
        	return results
        for (char, node) in self.children.items():
        	results.add(node.all_suffixes(prefix + char))
        return results

    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return list(node.all_suffixes(prefix))

def bfsBipartite (source):
	q = queue.Queue()
	colorMap = {}
	colorMap[source] = 1
	q.put (root)
	root.visited = true
	while not q.empty():
		nextNode = queue.get()
		for neighbor in nextNode.neighbors:
			if neighbor.visited == false and neighbor not in colorMap:
				neighbor.visited = true
				colorMap[neighbor] = 1 - colorMap[nextNode]
			elif neighbor.visited and neighbor in colorMap and colorMap[neighbor] == colorMap[nextNode]
				return False

def dijkstras (graph, weightFunction, startNode):
	seenNodes = set(list(startNode))
	distanceFromStart = {}
	predecssor = {}
	distanceFromStart[startNode] = 0
	for node in (graph.Nodes() - startNode):
		distanceFromStart[node] = weightFunction(node,startNode) # inifinty if 
		predecssor[node] = startNode
	while seenNodes < len(graph.Nodes()):
		choose cuurNode in graph.Nodes() - seenNodes such that min(distanceFromStart[cuurNode])
		seenNodes.add(cuurNode)
		for otherNode in (graph.Nodes() - seenNodes):
			if distanceFromStart[cuurNode] + weightFunction(cuurNode,otherNode) < distanceFromStart[otherNode]:
				distanceFromStart[otherNode] = distanceFromStart[cuurNode] + weightFunction(cuurNode,otherNode)
				predecssor[otherNode] = cuurNode

def main():
	break

if __name__ == "__main__":
    main()