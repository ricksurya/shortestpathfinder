import random
import matplotlib.pyplot as plt

def isVertex(probability):
    return random.random() < probability + 0.03

def isHome():
    return random.random() < 0.53

# x is the number of vertices; x/2 is number of homes
# Outputs a list of lists denoting ["name", x, y, bool (home or not)]
def generateSmallGraph():
    res = []
    numVertex = 1
    numHome = 0
    maxVertex = 50
    numHouses = maxVertex / 2
    numClusters = 4
    clusterDiameter = 7
    numVertexPerCluster = 12.0
    starting = ["point0", 8, 8, False]
    resHomes = []
    res.append(starting)
    for x in xrange(0, 20, 10): # Each cluster
        for y in xrange(0, 20, 10):
            vertexCount = 0
            homeCount = 0
            for px in xrange(x, x + clusterDiameter): # For generating vertices within the point
                for py in xrange(y, y + clusterDiameter):
                    if (isVertex(numVertexPerCluster/(clusterDiameter * clusterDiameter))) and vertexCount < numVertexPerCluster:
                        name = "point" + str(numVertex)
                        numVertex += 1
                        vertexCount += 1
                        newVertex = [name, px, py, False]
                        if (isHome()) and homeCount < numVertexPerCluster / 2:
                            newVertex[3] = True
                            homeCount += 1
                            numHome += 1
                            resHomes.append(newVertex)
                        res.append(newVertex)
    print("Vertices: ")
    print(len(res))
    print(res)
    print("Homes: ")
    print(len(resHomes))
    print(resHomes)
    xVertices = [x[1] for x in res]
    yVertices = [x[2] for x in res]
    plt.scatter(xVertices, yVertices, label= "stars", color= "green", marker= "*", s=30)
    xVertices = [x[1] for x in resHomes]
    yVertices = [x[2] for x in resHomes]
    plt.scatter(xVertices, yVertices, label= "stars", color= "red", marker= "o", s=30)
    plt.show()
    return res

def generateMediumGraph():
    res = []
    numVertex = 1
    numHome = 0
    totalVertex = 100
    numHouses = totalVertex / 2
    numClusters = 9
    clusterDiameter = 7
    numVertexPerCluster = 11.0
    starting = ["point0", 15, 15, False]
    resHomes = []
    res.append(starting)
    for x in xrange(0, 30, 10): # Each cluster
        for y in xrange(0, 30, 10):
            vertexCount = 0
            homeCount = 0
            for px in xrange(x, x + clusterDiameter): # For generating vertices within the point
                for py in xrange(y, y + clusterDiameter):
                    if (isVertex(numVertexPerCluster/(clusterDiameter * clusterDiameter))) and vertexCount < numVertexPerCluster:
                        name = "point" + str(numVertex)
                        numVertex += 1
                        vertexCount += 1
                        newVertex = [name, px, py, False]
                        if (isHome()) and homeCount < numVertexPerCluster / 2:
                            newVertex[3] = True
                            homeCount += 1
                            numHome += 1
                            resHomes.append(newVertex)
                        res.append(newVertex)
    print("Vertices: ")
    print(len(res))
    print(res)
    print("Homes: ")
    print(len(resHomes))
    print(resHomes)
    xVertices = [x[1] for x in res]
    yVertices = [x[2] for x in res]
    plt.scatter(xVertices, yVertices, label= "stars", color= "green", marker= "*", s=30)
    xVertices = [x[1] for x in resHomes]
    yVertices = [x[2] for x in resHomes]
    plt.scatter(xVertices, yVertices, label= "stars", color= "red", marker= "o", s=30)
    plt.show()
    return res

def generateLargeGraph():
    res = []
    numVertex = 1
    numHome = 0
    totalVertex = 200
    numHouses = totalVertex / 2
    numClusters = 16
    clusterDiameter = 14
    numVertexPerCluster = 12.0
    starting = ["point0", 20, 20, False]
    resHomes = []
    res.append(starting)
    for x in xrange(0, 80, 20): # Each cluster
        for y in xrange(0, 80, 20):
            vertexCount = 0
            homeCount = 0
            for px in xrange(x, x + clusterDiameter): # For generating vertices within the point
                for py in xrange(y, y + clusterDiameter):
                    if (isVertex(numVertexPerCluster/(clusterDiameter * clusterDiameter))) and vertexCount < numVertexPerCluster:
                        name = "point" + str(numVertex)
                        numVertex += 1
                        vertexCount += 1
                        newVertex = [name, px, py, False]
                        if (isHome()) and homeCount < numVertexPerCluster / 2:
                            newVertex[3] = True
                            homeCount += 1
                            numHome += 1
                            resHomes.append(newVertex)
                        res.append(newVertex)
    print("Vertices: ")
    print(len(res))
    print(res)
    print("Homes: ")
    print(len(resHomes))
    print(resHomes)
    xVertices = [x[1] for x in res]
    yVertices = [x[2] for x in res]
    plt.scatter(xVertices, yVertices, label= "stars", color= "green", marker= "*", s=30)
    xVertices = [x[1] for x in resHomes]
    yVertices = [x[2] for x in resHomes]
    plt.scatter(xVertices, yVertices, label= "stars", color= "red", marker= "o", s=30)
    plt.show()
    return res


generateLargeGraph()
