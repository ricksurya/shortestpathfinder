import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import math

from student_utils import *
from tsp import *
"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_locations: A list of locations such that node i of the graph corresponds to name at index i of the list
        list_of_homes: A list of homes
        starting_car_location: The name of the starting location for the car
        adjacency_matrix: The adjacency matrix from the input file
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    """
    # This will be the map for index name to real location name
    locationMap = {}
    # This is the index of the starting location
    startingIndex = -1
    # This is the list of homes as indexes
    homes = []

    for i in range(len(list_of_locations)):
        locationMap[i] = list_of_locations[i]
        if list_of_locations[i] == starting_car_location:
            startingIndex = i
        if list_of_locations[i] in list_of_homes:
            homes.append(i)

    # Create clusters
    distanceMatrix, pathMatrix = shortestDistance(adjacency_matrix)

    min_cost = math.inf

    for k in range(2, len(distanceMatrix)//2):
    	clusters = cluster(list(locationMap.keys()), homes, distanceMatrix, k)
    	raw_pathway = tsp(startingIndex, clusters, distanceMatrix)
    	real_pathway = realPath(raw_pathway, pathMatrix)
    	dropOffs = smart_dropOff(real_pathway, homes, distanceMatrix)

    	c = cost(real_pathway, dropOffs, distanceMatrix)
    	if c < min_cost:
    		min_cost = c
    		min_pathway = real_pathway
    		min_dropOffs = dropOffs

    print("Smart Cost : " + str(min_cost)) 
    print("Naive Cost : " + str(naive_cost(startingIndex, homes, distanceMatrix)))

    return min_pathway, min_dropOffs

    # Write to output file

def cost(real_pathway, dropOffs, distances):
	curr = 0
	total_cost = 0

	for i in range(len(real_pathway)-1):
		total_cost += (2 / 3) * distances[real_pathway[curr]][real_pathway[curr+1]]
		curr += 1

	for v in dropOffs:
		for h in dropOffs[v]:
			total_cost += distances[v][h]

	return total_cost

def naive_cost(source, homes, distances):
	total_cost = 0
	for h in homes:
		total_cost += distances[source][h]
	return total_cost

def realPath(tsp_path, all_paths):
	real_path = [tsp_path[0]]
	for i in range(len(tsp_path)-1):
		real_path.extend(all_paths[tsp_path[i]][tsp_path[i+1]])
	return real_path

# centroids: tsp_path
# clusters: dictionary of key = centroid and value is homes in the cluster
# homes:  set of homes
# distances: Matrix containing the distances

# dumb version
def dropOff(tsp_path, real_path, clusters, homes, distances):
	if tsp_path[0] in clusters:
		centroids = tsp_path[:-1]
	else:
		centroids = tsp_path[1:-1]

	drop = {}
	for v in real_path:
		drop_location = []
		if centroids and v == centroids[0]:
			for h in clusters[v]:
				if h in homes:
					drop_location.append(h)
					homes.remove(h)
			centroids.pop(0)

		if drop_location:
			drop[v] = drop_location

	return drop

# smart version
def smart_dropOff(real_pathway, homes, distances):
	drop = {}
	toReturn = {}

	for h in homes:
		min_dist = math.inf
		min_loc = -1
		for v in real_pathway:
			if distances[h][v] < min_dist:
				min_dist = distances[h][v]
				min_loc = v

		if min_loc not in drop:
			drop[min_loc] = [h]
		else:
			drop[min_loc].append(h)

	for v in real_pathway:
		if v in drop:
			toReturn[v] = drop[v]

	return toReturn

def shortestDistance(matrix):
	distances = []
	paths = []

	for u in range(len(matrix)):
		dist_u_v = []
		path_u_v = []
		for v in range (len(matrix)):
			if (u == v):
				dist_u_v.append([0] * (len(matrix) + 1))
			else:
				dist_u_v.append([float('inf')] * (len(matrix)+1))
			path_u_v.append([])

		distances.append(dist_u_v)
		paths.append(path_u_v)

	for u in range(len(matrix)):
		for v in range(len(matrix)):
			if u != v and matrix[u][v] != 'x':
				distances[u][v][0] = matrix[u][v]
				paths[u][v].append(v)

	for k in range(1, len(matrix)+1):
		for u in range(len(matrix)):
			for v in range(len(matrix)):
				uses_k = distances[u][k-1][k-1] + distances[k-1][v][k-1]
				bypass_k = distances[u][v][k-1]

				if (uses_k < bypass_k):
					distances[u][v][k] = uses_k
					paths[u][v] = paths[u][k-1] + paths[k-1][v]
				else:
					distances[u][v][k] = bypass_k

	shortestDistance = []
	for u in range(len(matrix)):
		node = []
		for v in range(len(matrix)):
			node.append(min(distances[u][v]))
		shortestDistance.append(node)

	return shortestDistance, paths

def cluster(list_locations, list_houses, shortestDistance, k_clusters = 7):
	#shorestDistance is a matrix where each row i column j represents the shortest distance from node i to node j

	#first choose k random locations and set them as centroid
	centroids = np.random.choice(list_locations, size = k_clusters, replace = False)
	iterations = 5
	#dictionary on centroid, value is set of points in that cluster
	clusters = {}
	houses_set = set(list_houses)

	for i in centroids:
		clusters[i] = set()
	#assigns each node to a centroid
	for j in range(len(shortestDistance)):
		closest_centroid_index = np.argmin([shortestDistance[j][c] for c in centroids])
		clusters[centroids[closest_centroid_index]].add(j)

	#print("*****FIRST********")
	#for t in clusters.keys():
	#	print("cluster", t)
	#	for k in clusters[t]:
	#		print("Node", k)
	#	print()

	#reassign centroids in each cluster iterations times
	for itera in range(iterations):
		new_centroids = []
		for centroid_cluster in centroids:
			possible_new_centroids = clusters[centroid_cluster]
			homes_in_cluster = set()
			for i in possible_new_centroids:
				if (i in houses_set):
					homes_in_cluster.add(i)
			if len(homes_in_cluster) == 0:
				new_centroids.append(centroid_cluster)
				continue
			else:
				new_centroid = centroid_cluster
				new_centroid_dist = averageDistanceToHomes(centroid_cluster, homes_in_cluster, shortestDistance)
				for potential_centroid in possible_new_centroids:
					potential_dist = averageDistanceToHomes(potential_centroid, homes_in_cluster, shortestDistance)
					if (potential_dist < new_centroid_dist):
						new_centroid = potential_centroid
						new_centroid_dist = potential_dist
				new_centroids.append(new_centroid)
				#print(new_centroid_dist)

		#print("old centroids:", centroids)
		#print("new centroids:", new_centroids)
		centroids = new_centroids[:]
		clusters = {}

		for i in centroids:
			clusters[i] = set()

		for j in range(len(shortestDistance)):
			closest_centroid_index = np.argmin([shortestDistance[j][centroids[i]] for i in range(len(centroids))])
			clusters[centroids[closest_centroid_index]].add(j)


	#	print("*********", itera, "**********")
	#	for t in clusters.keys():
	#		print("cluster", t)
	#		for k in clusters[t]:
	#			print("Node", k)
	#		print()




	#for t in clusters.keys():
	#	print("cluster", t)
	#	for k in clusters[t]:
	#		print("Node", k)
	#	print()


	#colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
	#plt.scatter(xVertices[list_houses], yVertices[list_houses], label= "stars", color= "blue", marker= "*", s=30)
	#for n in range(len(centroids)):
#		for a in clusters[centroids[n]]:#
#			if a in houses_set:
#				plt.scatter(xVertices[a], yVertices[a], label= "stars", color= colors[n], marker= ".", s=30)
#			else:
#				plt.scatter(xVertices[a], yVertices[a], label= "stars", color= colors[n], marker= "v", s=10)
#			plt.scatter(xVertices[centroids[n]], yVertices[centroids[n]], label= "stars", color= colors[n], marker= "*", s=50)


#	plt.show()
	#print("-----------------------------------")
	#for cent in clusters.keys():
	#	print("Cluster with removed VX", cent)
	#	for loc in list(clusters[cent]):
#			if (loc not in houses_set):
#				clusters[cent].remove(loc)
#			else:
#				print("Home Node:", loc)
#		print()

	#clusters is a dictionary of centroid: set(houses)

	#returned = []
	returned_clusters = {}
	for cent in clusters.keys():
		if len(clusters[cent]) > 0:
			returned_clusters[cent] = clusters[cent]
#			returned.append([cent, list(clusters[cent])])


#	for i in returned:
#		print(i[0], ": ", i[1])
	#print(returned)
	#print(returned_clusters)
	return returned_clusters #second value is dictionary, centroid




def averageDistanceToHomes(centroid, homes_in_cluster, shortestDistance):
	if len(homes_in_cluster) == 0:
		return 0
	dists = shortestDistance[centroid]
	sum_dist = sum([dists[home] for home in homes_in_cluster])
	return sum_dist / len(homes_in_cluster)


"""
======================================================================
   No need to change any code below this line
======================================================================
"""

"""
Convert solution with path and dropoff_mapping in terms of indices
and write solution output in terms of names to path_to_file + file_number + '.out'
"""
def convertToFile(path, dropoff_mapping, path_to_file, list_locs):
    string = ''
    for node in path:
        string += list_locs[node] + ' '
    string = string.strip()
    string += '\n'

    dropoffNumber = len(dropoff_mapping.keys())
    string += str(dropoffNumber) + '\n'
    for dropoff in dropoff_mapping.keys():
        strDrop = list_locs[dropoff] + ' '
        for node in dropoff_mapping[dropoff]:
            strDrop += list_locs[node] + ' '
        strDrop = strDrop.strip()
        strDrop += '\n'
        string += strDrop
    utils.write_to_file(path_to_file, string)

def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)

    input_data = utils.read_file(input_file)
    num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = data_parser(input_data)
    car_path, drop_offs = solve(list_locations, list_houses, starting_car_location, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = utils.input_to_output(input_file, output_directory)

    convertToFile(car_path, drop_offs, output_file, list_locations)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)
# solve_from_file("inputs/50.in", "outputstests/")
# solve_from_file("inputs/100.in", "outputstests/")
# solve_from_file("inputs/200.in", "outputstests/")
