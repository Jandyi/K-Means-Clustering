import matplotlib.pyplot as plt
import math
import random
from pathlib import Path

class KMeans:
    def __init__(self, K, totalIterations, Minimumloss):
        self.K = K
        self.totalIterations = totalIterations
        self.Minimumloss = Minimumloss
        self.listofX = []
        self.listofY = []
        self.pointCount = 0
        self.Centroids = []
        self.clusters = []
        self.Xlabel = "X"
        self.Ylabel = "Y"
        self.Colors = ["orange", "pink", "brown", "gray", "cyan", "lime", "navy"]
    
    def Average(self, lst):
        if len(lst) == 0:
            return 0
        s = 0
        for i in lst:
            s = s + i
        return s / len(lst)
    
    def Distance(self, x1, x2, y1, y2):
        distanceX = x1 - x2
        distanceY = y1 - y2
        return math.sqrt(distanceX * distanceX + distanceY * distanceY)
    
    def readPoints(self, fileName):
        self.listofX = []
        self.listofY = []
        with open(fileName, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i in range(1, len(lines)):
            parts = lines[i].strip().split(',')
            if len(parts) >= 2:
                try:
                    self.listofX.append(float(parts[0]))
                    self.listofY.append(float(parts[1]))
                except ValueError:
                    pass
        self.pointCount = len(self.listofX)
    
    def initCentroids(self):
        self.Centroids = []
        K = self.K
        if len(self.listofX) < K:
            K = len(self.listofX)
        chosen = random.sample(range(len(self.listofX)), K)
        for i in chosen:
            self.Centroids.append([self.listofX[i], self.listofY[i]])
    
    def initClusters(self):
        clusters = []
        for i in range(self.K):
            clusters.append([[], []])
        return clusters
    
    def rebuildClusters(self):
        self.clusters = self.initClusters()
        for i in range(self.pointCount):
            pointX = self.listofX[i]
            pointY = self.listofY[i]
            mind = 999999999
            c = 0
            for j in range(self.K):
                centroidX = self.Centroids[j][0]
                centroidY = self.Centroids[j][1]
                d = self.Distance(pointX, centroidX, pointY, centroidY)
                if d < mind:
                    mind = d
                    c = j
            self.clusters[c][0].append(pointX)
            self.clusters[c][1].append(pointY)
    
    def reCalclculateCentroids(self):
        newcentroid = []
        for i in range(self.K):
            xs = self.clusters[i][0]
            ys = self.clusters[i][1]
            if len(xs) > 0:
                newX = self.Average(xs)
                newY = self.Average(ys)
            else:
                if self.Centroids and i < len(self.Centroids):
                    newX = self.Centroids[i][0]
                    newY = self.Centroids[i][1]
                else:
                    newX = 0
                    newY = 0
            newcentroid.append([newX, newY])
        return newcentroid
    
    def calculateLossValue(self, newcentroid):
        t = 0
        for i in range(self.K):
            oldX = self.Centroids[i][0]
            oldY = self.Centroids[i][1]
            newX = newcentroid[i][0]
            newY = newcentroid[i][1]
            t = t + self.Distance(oldX, newX, oldY, newY)
        return t
    
    def K_Means_iteration(self):
        self.rebuildClusters()
        newcentroid = self.reCalclculateCentroids()
        loss = self.calculateLossValue(newcentroid)
        self.Centroids = newcentroid
        return loss
    
    def showClusters(self):
        Colors = self.Colors
        if len(Colors) < self.K:
            Colors = Colors + [Colors[-1]] * (self.K - len(Colors))
        for i in range(self.K):
            if len(self.clusters[i][0]) > 0:
                plt.scatter(self.clusters[i][0], self.clusters[i][1], c=Colors[i], label='Cluster ' + str(i + 1))
        plt.xlabel(self.Xlabel)
        plt.ylabel(self.Ylabel)
        plt.title('Clustering but OOP')
        plt.legend()
        plt.show()
    
    def showDataPoints(self):
        plt.scatter(self.listofX, self.listofY)
        plt.xlabel(self.Xlabel)
        plt.ylabel(self.Ylabel)
        plt.title("Points but OOP")
        plt.show()
    
    def run(self):
        self.initCentroids()
        iterations = self.totalIterations
        while iterations > 0:
            loss = self.K_Means_iteration()
            print("Epoch = %d" % (self.totalIterations - iterations + 1))
            print("Loss Function = %0.4f" % loss)
            if loss < self.Minimumloss:
                break
            iterations = iterations - 1

kmeans = KMeans(K=6, totalIterations=50, Minimumloss=0.0001)
DATA_FILE = Path(__file__).resolve().parent / "data.csv"
kmeans.readPoints(DATA_FILE)
kmeans.showDataPoints()
kmeans.run()
kmeans.showClusters()