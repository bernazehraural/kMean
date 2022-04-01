import argparse
from math import sqrt

argGet = argparse.ArgumentParser()
argGet.add_argument('--data', '--data', type=str)

# get the name of file
args = argGet.parse_args()
filename = args.data

# open the file and save the data into inputList
with open(filename, 'r') as file:
    inputList = file.readlines()
    inputList = [row.split(',') for row in inputList]

#initialization
sumOfClusterDist = 0
criteriaList = []
clusterList = []
mapping = []
k = 3
c1 = (0, 5)
c2 = (0, 4)
c3 = (0, 3)
clusters = [c1, c2, c3]

pointList = []
# ignored first column, get X and Y values of the points
# and assigned into the pointList
for i in range(0, len(inputList)):
    xAxis = float(inputList[i][1])
    yAxis = float(inputList[i][2])
    pointList.append((xAxis, yAxis))


def euclidianDistance(cluster, point):
    return sqrt((cluster[0] - point[0])**2 + (cluster[1] - point[1])**2)


def makeMap():
    sumOfClusterDist = 0
    # for each points should be calculated the Euclidian dist
    # for all 3 cluster
    for i in range(len(pointList)):
        distC1Point = euclidianDistance(clusters[0], pointList[i])
        distC2Point = euclidianDistance(clusters[1], pointList[i])
        distC3Point = euclidianDistance(clusters[2], pointList[i])
        distances = [distC1Point, distC2Point, distC3Point]
        sumOfClusterDist = sumOfClusterDist + min(distances)**2
        index = distances.index(min(distances))
        mapping.append(index)
    return sumOfClusterDist


def changeCluster():
    # change clusters
    c1New, c2New, c3New = [], [], []
    cluster1, cluster2, cluster3 = (0,0), (0,0), (0,0)
    c1x, c1y, c2x, c2y, c3x, c3y = 0, 0, 0, 0, 0, 0
    for x in range(len(mapping)):
        a = pointList[x][0]
        b = pointList[x][1]
        if mapping[x] == 0:
            c1New.append((a, b))
            c1x = c1x + a
            c1y = c1y + b
        if mapping[x] == 1:
            c2New.append((a, b))
            c2x = c2x + a
            c2y = c2y + b
        if mapping[x] == 2:
            c3New.append((a, b))
            c3x = c3x + a
            c3y = c3y + b


    if len(c1New) != 0:
        cluster1 = (c1x / len(c1New), c1y / len(c1New))
    else:
        cluster1 = (0, 0)
    if len(c2New) != 0:
        cluster2 = (c2x / len(c2New), c2y / len(c2New))
    else:
        cluster2 = (0, 0)
    if len(c3New) != 0:
        cluster3 = (c3x / len(c3New), c3y / len(c3New))
    else:
        cluster3 = (0, 0)

    return cluster1, cluster2, cluster3


isDiff = True

while isDiff:
    mapping = []
    sumOfClusterDist = makeMap()
    criteriaList.append(sumOfClusterDist)
    k, l, m = changeCluster()
    if (k == clusters[0]) and (l == clusters[1]) and (m == clusters[2]):
        isDiff = False
    else:
        clusters[0] = k
        clusters[1] = l
        clusters[2] = m
        clusterList.append([k, l, m])

for j in criteriaList:
    print(j)
print(c1[0],",",c1[1],"	  ",c2[0],",",c2[1],"   ",c3[0],",",c3[1],sep="")
for k in clusterList:
    print(k[0][0],",",k[0][1],"   ",k[1][0],",",k[1][1],"   ",k[2][0],",",k[2][1],sep="")
