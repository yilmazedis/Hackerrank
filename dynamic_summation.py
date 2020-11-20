# Square Root under Modulo p | Set 2 (Shanks Tonelli algorithm)
# Fermat's little theorem to find Remainder

from collections import defaultdict 
  
# Function to build the graph 
def build_graph(edges): 
	graph = defaultdict(list) 
	  
	# Loop to iterate over every  
	# edge of the graph 
	for edge in edges: 
		a, b = edge[0], edge[1] 
		  
		# Creating the graph  
		# as adjacency list 
		graph[a].append(b) 
		graph[b].append(a)

	for g in graph:
		graph[g].append(0)

	return graph

def addEdges(edges, node1, node2):
	edges.append([node1, node2])


def putValue(graph, r, t, value):

	nodes = graph[t]

	if not nodes:
		return

	nodes[-1] = value

	#print(nodes)

	for n in nodes[0:-1]:
		if n != r:
			putValue(graph, t, n, value)


def getSumOfValues(graph, r, t):

	nodes = graph[t]

	if not nodes:
		return 0

	#print(nodes[-1])

	total = nodes[-1]
	for n in nodes[0:-1]:
		if n != r:
			total += getSumOfValues(graph, t, n)	

	return total
  
if __name__ == "__main__":

	edges = [] 

	for i in range(int(input()) - 1):
		nodes = input().strip().split()
		addEdges(edges, nodes[0], nodes[1])


	graph = build_graph(edges) 
	
	#putValue(graph, "2", "3", 22)

	#print(graph)


	for i in range(int(input())):
		query = input().strip().split()

		if query[0] == "U":
			r = query[1]
			t = query[2]

			a = int(query[3])
			b = int(query[4])

			value = a**b + (a + 1)**b + (b + 1)**a
			
			putValue(graph, r, t, value)

			# print(graph)
		else:
			r = query[1]
			t = query[2]

			report = getSumOfValues(graph, r, t) % int(query[3])

			print(report)


			# 2119669123
			# 2130014475
			# 271204709
			# 309663683
			# 18571328

			# 969824663.6 
