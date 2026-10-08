import matplotlib.pyplot as plt
import math
import random
from pathlib import Path

def Average(lst):
    if len(lst) == 0:
        return 0
    s = 0
    for i in lst:
        s = s + i
    return s / len(lst)

def Distance(x1, x2, y1, y2):
    distanceX = x1 - x2
    distanceY = y1 - y2
    return math.sqrt(distanceX * distanceX + distanceY * distanceY)

def readPoints(fileName):
    listofX = []
    listofY = []
    with open(fileName, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i in range(1, len(lines)):
        parts = lines[i].strip().split(',')
        if len(parts) >= 2:
            try:
                listofX.append(float(parts[0]))
                listofY.append(float(parts[1]))
            except ValueError:
                pass
    return listofX, listofY, len(listofX)

def initCentroids(listofX, listofY, K):
    centroids = []
    if len(listofX) < K:
        K = len(listofX)
    chosen = random.sample(range(len(listofX)), K)
    for i in chosen:
        centroids.append([listofX[i], listofY[i]])
    return centroids

def initClusters(K):
    clusters = []
    for i in range(K):
        clusters.append([[], []])
    return clusters

def rebuildClusters(pointCount, Centroids, listofX, listofY, K):
    clusters = initClusters(K)
    for i in range(pointCount):
        pointX = listofX[i]
        pointY = listofY[i]
        mind = 999999999
        c = 0
        for j in range(K):
            centroidX = Centroids[j][0]
            centroidY = Centroids[j][1]
            d = Distance(pointX, centroidX, pointY, centroidY)
            if d < mind:
                mind = d
                c = j
        clusters[c][0].append(pointX)
        clusters[c][1].append(pointY)
    return clusters

def reCalclculateCentroids(clusters, K, old):
    newcentroid = []
    for i in range(K):
        xs = clusters[i][0]
        ys = clusters[i][1]
        if len(xs) > 0:
            newX = Average(xs)
            newY = Average(ys)
        else:
            if old and i < len(old):
                newX = old[i][0]
                newY = old[i][1]
            else:
                newX = 0
                newY = 0
        newcentroid.append([newX, newY])
    return newcentroid

def calculateLossValue(newcentroid, oldc, K):
    t = 0
    for i in range(K):
        oldX = oldc[i][0]
        oldY = oldc[i][1]
        newX = newcentroid[i][0]
        newY = newcentroid[i][1]
        t = t + Distance(oldX, newX, oldY, newY)
    return t

def K_Means_iteration(pointCount, listofX, listofY, Centroids, K):
    clusters = rebuildClusters(pointCount, Centroids, listofX, listofY, K)
    newcentroid = reCalclculateCentroids(clusters, K, Centroids)
    loss = calculateLossValue(newcentroid, Centroids, K)
    return clusters, loss, newcentroid

def showClusters(clusters, Xlabel, Ylabel, K, Colors):
    if len(Colors) < K:
        Colors = Colors + [Colors[-1]] * (K - len(Colors))
    for i in range(K):
        if len(clusters[i][0]) > 0:
            plt.scatter(clusters[i][0], clusters[i][1], c=Colors[i], label='Cluster ' + str(i + 1))
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.title('Clustering')
    plt.legend()
    plt.show()

DATA_FILE = Path(__file__).resolve().parent / "data.csv"
listofX, listofY, pointCount = readPoints(DATA_FILE)
Xlabel = "X"
Ylabel = "Y"

plt.scatter(listofX, listofY)
plt.xlabel(Xlabel)
plt.ylabel(Ylabel)
plt.title("Points")
plt.show()

totalIterations = 50
iterations = totalIterations
K = 6
Minimumloss = 0.0001

Centroids = initCentroids(listofX, listofY, K)
while iterations > 0:
    clusters, loss, Centroids = K_Means_iteration(pointCount, listofX, listofY, Centroids, K)
    print("Epoch = %d" % (totalIterations - iterations + 1))
    print("Loss Function = %0.4f" % loss)
    if loss < Minimumloss:
        break
    iterations = iterations - 1

Colors = ["orange", "pink", "brown", "gray", "cyan", "lime", "navy"]
showClusters(clusters, Xlabel, Ylabel, K, Colors)