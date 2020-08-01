import random
import student_utils
import networkx as nx
import matplotlib.pyplot as plt
import utils


# outputs the adjacency matrix
# nodes = [[string name, x, y, house or not], [], ...]
def connectNodes(nodes):
	matrix = []
	for row in range(len(nodes)):
		r = []
		for col in range(len(nodes)):
			r.append("x")
		matrix.append(r)

	connected = []
	vertices = list(range(len(nodes)))

	# first vertex added to connected
	i = random.randrange(len(vertices))
	connected.append(vertices[i])
	vertices.pop(i)

	# make sure everything is at least connected
	while vertices:
		i = random.randrange(len(vertices))
		j = random.randrange(len(connected))

		u = vertices[i]
		v = connected[j]

		u_x = nodes[u][1]
		u_y = nodes[u][2]

		v_x = nodes[v][1]
		v_y = nodes[v][2]

		distance = pow((v_x - u_x) ** 2 + (v_y - u_y) ** 2, 0.5)
		matrix[u][v] = round(distance, 5)
		matrix[v][u] = round(distance, 5)

		vertices.pop(i)
		connected.append(u)

	# add random edges to increase complexity
	# can reduce or increase the number of edges by changing the range in the for loop
	for i in range (int(0.1 * (len(nodes) ** 2))):
		u = random.randrange(len(nodes))
		v = random.randrange(len(nodes))

		while (u == v) or (matrix[u][v] != 'x'):
			u = random.randrange(len(nodes))
			v = random.randrange(len(nodes))

		u_x = nodes[u][1]
		u_y = nodes[u][2]

		v_x = nodes[v][1]
		v_y = nodes[v][2]

		distance = pow((v_x - u_x) ** 2 + (v_y - u_y) ** 2, 0.5)
		matrix[u][v] = round(distance, 5)
		matrix[v][u] = round(distance, 5)

	return matrix

def listToString(s):
	for i in range(len(s)):
		s[i] = str(s[i])
    # initialize an empty string
	str1 = " "
    # return string
	return (str1.join(s))

def writeToInput(nodes, matrix):
	fileName = "inputs/200.in"
	utils.write_to_file(fileName, str(len(nodes)) + "\n")
	homeCount = 0
	homes = ""
	nodeName = ""
	for node in nodes:
		space = " "
		if node[0] == "point0":
			space = ""
		nodeName += space + node[0]
		if node[3]:
			if homeCount == 0:
				space = ""
			homeCount += 1
			homes += space + node[0]
	utils.write_to_file(fileName, str(homeCount) + "\n", True)
	utils.write_to_file(fileName, nodeName + "\n", True)
	utils.write_to_file(fileName, homes + "\n", True)
	for adjList in matrix:
		utils.write_to_file(fileName, listToString(adjList) + "\n", True)


# example
nodeSmall = [['point0', 8, 8, False], ['point1', 0, 0, True], ['point2', 1, 1, False], ['point3', 1, 4, True], ['point4', 1, 5, True], ['point5', 2, 4, True], ['point6', 3, 0, True], ['point7', 3, 5, True], ['point8', 4, 0, False], ['point9', 4, 1, False], ['point10', 4, 3, False], ['point11', 4, 5, False], ['point12', 5, 3, False], ['point13', 0, 14, False], ['point14', 1, 12, False], ['point15', 1, 16, False], ['point16', 2, 10, True], ['point17', 3, 11, False], ['point18', 3, 13, False], ['point19', 4, 11, True], ['point20', 4, 12, False], ['point21', 4, 13, True], ['point22', 4, 15, False], ['point23', 6, 10, True], ['point24', 6, 11, True], ['point25', 10, 4, True], ['point26', 11, 5, True], ['point27', 11, 6, False], ['point28', 12, 1, False], ['point29', 12, 4, False], ['point30', 13, 3, True], ['point31', 13, 6, False], ['point32', 14, 3, False], ['point33', 15, 1, True], ['point34', 15, 4, False], ['point35', 15, 6, True], ['point36', 16, 3, False], ['point37', 10, 12, True], ['point38', 10, 15, False], ['point39', 11, 15, False], ['point40', 12, 10, False], ['point41', 12, 12, True], ['point42', 12, 16, True], ['point43', 13, 15, True], ['point44', 14, 14, False], ['point45', 15, 10, False], ['point46', 15, 12, True], ['point47', 15, 13, True], ['point48', 15, 14, False]]

nodeMedium = [['point0', 15, 15, False], ['point1', 0, 0, False], ['point2', 1, 0, False], ['point3', 2, 0, False], ['point4', 2, 2, True], ['point5', 2, 3, True], ['point6', 2, 4, True], ['point7', 2, 6, True], ['point8', 3, 5, True], ['point9', 4, 1, True], ['point10', 4, 6, False], ['point11', 5, 3, False], ['point12', 0, 10, True], ['point13', 0, 11, False], ['point14', 0, 12, True], ['point15', 1, 12, False], ['point16', 1, 13, False], ['point17', 1, 14, False], ['point18', 2, 10, False], ['point19', 3, 11, True], ['point20', 3, 16, False], ['point21', 4, 16, False], ['point22', 6, 11, True], ['point23', 1, 22, False], ['point24', 2, 21, True], ['point25', 2, 22, True], ['point26', 3, 22, True], ['point27', 3, 23, True], ['point28', 3, 24, True], ['point29', 3, 25, False], ['point30', 4, 22, False], ['point31', 4, 23, False], ['point32', 5, 20, False], ['point33', 5, 26, False], ['point34', 10, 0, False], ['point35', 10, 2, True], ['point36', 12, 3, False], ['point37', 12, 5, False], ['point38', 13, 4, False], ['point39', 13, 6, False], ['point40', 16, 0, False], ['point41', 16, 6, False], ['point42', 10, 12, True], ['point43', 10, 13, False], ['point44', 11, 11, True], ['point45', 11, 12, True], ['point46', 12, 14, False], ['point47', 12, 15, True], ['point48', 13, 12, True], ['point49', 13, 14, False], ['point50', 14, 13, True], ['point51', 15, 11, False], ['point52', 16, 12, False], ['point53', 10, 25, True], ['point54', 12, 25, False], ['point55', 13, 22, True], ['point56', 14, 20, True], ['point57', 14, 22, False], ['point58', 14, 26, True], ['point59', 15, 21, False], ['point60', 15, 23, True], ['point61', 16, 21, True], ['point62', 20, 1, False], ['point63', 21, 0, False], ['point64', 21, 3, True], ['point65', 22, 2, True], ['point66', 22, 4, False], ['point67', 23, 2, False], ['point68', 23, 3, True], ['point69', 24, 6, False], ['point70', 25, 0, True], ['point71', 25, 3, True], ['point72', 26, 0, True], ['point73', 20, 10, False], ['point74', 21, 11, False], ['point75', 21, 12, True], ['point76', 21, 13, True], ['point77', 22, 10, True], ['point78', 22, 11, False], ['point79', 23, 10, False], ['point80', 23, 14, False], ['point81', 24, 13, False], ['point82', 25, 11, False], ['point83', 26, 14, False], ['point84', 20, 25, True], ['point85', 21, 24, True], ['point86', 23, 21, False], ['point87', 23, 23, False], ['point88', 23, 26, False], ['point89', 25, 21, False], ['point90', 25, 22, False], ['point91', 26, 24, False], ['point92', 26, 25, True], ['point93', 26, 26, True]]

nodeLarge = [['point0', 20, 20, False], ['point1', 0, 5, True], ['point2', 1, 0, False], ['point3', 2, 4, True], ['point4', 2, 8, False], ['point5', 2, 9, True], ['point6', 3, 5, True], ['point7', 4, 13, False], ['point8', 8, 4, False], ['point9', 8, 8, False], ['point10', 10, 0, True], ['point11', 11, 0, True], ['point12', 11, 5, False], ['point13', 0, 20, True], ['point14', 0, 25, False], ['point15', 1, 20, True], ['point16', 1, 25, True], ['point17', 1, 26, True], ['point18', 1, 30, True], ['point19', 2, 26, False], ['point20', 3, 24, False], ['point21', 3, 26, True], ['point22', 4, 20, False], ['point23', 5, 21, False], ['point24', 5, 31, False], ['point25', 0, 48, False], ['point26', 0, 51, False], ['point27', 1, 40, True], ['point28', 2, 43, False], ['point29', 2, 44, True], ['point30', 2, 48, True], ['point31', 2, 49, True], ['point32', 3, 40, False], ['point33', 3, 48, True], ['point34', 3, 49, True], ['point35', 5, 48, False], ['point36', 5, 50, False], ['point37', 0, 61, False], ['point38', 0, 68, True], ['point39', 0, 71, True], ['point40', 3, 72, True], ['point41', 4, 63, True], ['point42', 4, 68, True], ['point43', 5, 63, True], ['point44', 5, 64, False], ['point45', 5, 72, False], ['point46', 5, 73, False], ['point47', 7, 66, False], ['point48', 7, 69, False], ['point49', 21, 7, True], ['point50', 21, 9, False], ['point51', 22, 7, True], ['point52', 23, 13, True], ['point53', 24, 2, False], ['point54', 24, 3, True], ['point55', 24, 5, True], ['point56', 24, 6, True], ['point57', 24, 13, False], ['point58', 25, 8, False], ['point59', 26, 5, False], ['point60', 26, 6, False], ['point61', 20, 26, False], ['point62', 20, 33, False], ['point63', 21, 30, False], ['point64', 22, 21, False], ['point65', 22, 32, False], ['point66', 23, 27, False], ['point67', 23, 29, True], ['point68', 23, 30, False], ['point69', 25, 22, True], ['point70', 27, 24, False], ['point71', 27, 25, False], ['point72', 28, 32, True], ['point73', 20, 42, True], ['point74', 23, 49, False], ['point75', 25, 46, True], ['point76', 25, 49, True], ['point77', 26, 52, False], ['point78', 27, 44, True], ['point79', 29, 41, True], ['point80', 29, 44, False], ['point81', 29, 51, False], ['point82', 29, 52, False], ['point83', 30, 48, True], ['point84', 33, 46, False], ['point85', 20, 62, True], ['point86', 20, 63, True], ['point87', 20, 73, True], ['point88', 22, 60, False], ['point89', 22, 73, True], ['point90', 24, 61, False], ['point91', 24, 67, True], ['point92', 24, 71, False], ['point93', 24, 72, False], ['point94', 25, 60, True], ['point95', 25, 73, False], ['point96', 26, 67, False], ['point97', 40, 5, False], ['point98', 41, 4, False], ['point99', 41, 12, False], ['point100', 42, 8, True], ['point101', 43, 5, False], ['point102', 43, 11, True], ['point103', 44, 8, True], ['point104', 46, 10, False], ['point105', 46, 12, False], ['point106', 47, 4, False], ['point107', 47, 8, False], ['point108', 48, 5, True], ['point109', 40, 24, True], ['point110', 40, 28, True], ['point111', 41, 20, True], ['point112', 41, 25, True], ['point113', 42, 26, True], ['point114', 42, 27, False], ['point115', 43, 27, True], ['point116', 45, 23, False], ['point117', 50, 32, False], ['point118', 51, 27, False], ['point119', 40, 45, True], ['point120', 40, 51, True], ['point121', 41, 47, False], ['point122', 41, 48, True], ['point123', 44, 47, True], ['point124', 45, 45, True], ['point125', 45, 49, False], ['point126', 45, 50, True], ['point127', 45, 52, False], ['point128', 48, 41, False], ['point129', 48, 47, False], ['point130', 48, 51, False], ['point131', 41, 70, True], ['point132', 42, 63, True], ['point133', 42, 65, False], ['point134', 42, 73, True], ['point135', 44, 72, True], ['point136', 46, 65, False], ['point137', 46, 69, False], ['point138', 46, 70, True], ['point139', 46, 72, True], ['point140', 47, 61, False], ['point141', 47, 69, False], ['point142', 48, 70, False], ['point143', 60, 2, False], ['point144', 60, 11, True], ['point145', 61, 13, False], ['point146', 62, 11, False], ['point147', 63, 0, False], ['point148', 63, 7, True], ['point149', 65, 7, True], ['point150', 65, 10, False], ['point151', 66, 6, True], ['point152', 66, 8, True], ['point153', 66, 10, True], ['point154', 67, 4, False], ['point155', 60, 23, True], ['point156', 60, 31, False], ['point157', 61, 24, True], ['point158', 62, 21, True], ['point159', 62, 25, False], ['point160', 64, 31, True], ['point161', 64, 33, False], ['point162', 65, 20, True], ['point163', 65, 23, True], ['point164', 67, 23, False], ['point165', 68, 25, False], ['point166', 69, 30, False], ['point167', 62, 49, False], ['point168', 63, 52, False], ['point169', 64, 48, False], ['point170', 65, 40, False], ['point171', 65, 44, False], ['point172', 65, 48, True], ['point173', 66, 43, False], ['point174', 66, 47, False], ['point175', 67, 40, False], ['point176', 67, 48, False], ['point177', 69, 40, True], ['point178', 69, 43, False], ['point179', 60, 64, True], ['point180', 60, 67, True], ['point181', 61, 63, False], ['point182', 61, 71, False], ['point183', 62, 62, True], ['point184', 63, 70, True], ['point185', 64, 66, True], ['point186', 64, 70, False], ['point187', 66, 71, True], ['point188', 67, 60, False], ['point189', 67, 65, False], ['point190', 67, 66, False]]


matrix = connectNodes(nodeLarge)
graph = student_utils.adjacency_matrix_to_graph(matrix)[0]
# nx.draw(graph)
# plt.show()
print(student_utils.is_metric(graph))
writeToInput(nodeLarge, matrix)
