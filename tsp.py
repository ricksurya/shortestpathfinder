import math

def tsp(starting, clusters, distMatrix):
    path = []
    centroids = [x for x in list(clusters.keys())]
    centroids.sort()
    # Check if starting point is in centroids
    if starting in centroids:
        centroids.remove(starting)
    centroids.insert(0, starting)


    # Create dictionary for index to centroids index
    centDict = {}
    for i in range(len(centroids)):
        centDict[i] = centroids[i]

    # Create distance matrix for MST
    mstMatrix = []
    for i in range(len(centroids)):
        tmp = []
        for j in range(len(centroids)):
            if i == j:
                tmp.append(math.inf)
            else:
                tmp.append(distMatrix[centroids[i]][centroids[j]])
        mstMatrix.append(tmp)

    # Find MST
    adjList = primMST(mstMatrix)

    # DFS Traversal of the tree
    traversal = dfs(adjList)

    # Drop repeated vertices from traversal
    traversal = deleteRepetition(traversal)

    # Translate DFS traversal into original centroid index
    for i in range(len(traversal)):
        traversal[i] = centDict.get(traversal[i])

    return traversal


def dfs(adj_lst):
	visited = [False] * len(adj_lst)
	path = []

	def explore(v):
		visited[v] = True
		path.append(v)
		for u in adj_lst[v]:
			if not visited[u]:
				explore(u)
				path.append(v)

	explore(0)
	return path

def deleteRepetition(path):
	toReturn = []
	for i in path:
		if i not in toReturn:
			toReturn.append(i)
	toReturn.append(0)
	return toReturn


def isValidEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] == False and inMST[v] == False:
        return False
    elif inMST[u] == True and inMST[v] == True:
        return False
    return True

# Prim algorithm source: Geeks for Geeks
def primMST(cost):
    V = len(cost)
    res = []
    for i in range(len(cost)):
        res.append([])
    inMST = [False] * V

    # Include first vertex in MST
    inMST[0] = True

    # Keep adding edges while number of included
    # edges does not become V-1.
    edge_count = 0
    while edge_count < V - 1:
        #print("V - 1 = " + str(V-1))
        #print("edge count = " + str(edge_count))
        # Find minimum weight valid edge.
        minn = math.inf
        a = -1
        b = -1
        for i in range(V):
            #print("i = " + str(i))
            for j in range(V):
                #print("i = " + str(i) + " j = " + str(j) + " cost = " + str(cost[i][j]))
                if cost[i][j] < minn:
                    if isValidEdge(i, j, inMST):
                        minn = cost[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            edge_count += 1
            inMST[b] = inMST[a] = True
            res[a].append(b)
            res[b].append(a)
    return res

# clusters = {0: 0, 1:0, 2:0, 3:0}
# starting = 1
# distMatrix = [[0, 99, 15, 20], [99, 0, 25, 25], [15, 25, 0, 30], [20, 25, 30, 0]]
# print(tsp(starting, clusters, distMatrix))
