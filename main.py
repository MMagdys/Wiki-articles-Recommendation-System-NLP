import random
import numpy as np
import pandas as pd


class Kmeans:
    def __init__(self, k, max_iter=300, distance_method='manhattan'):
        self.k = k
        self.distance_method = distance_method
        self.centers = []
        self.max_iter = max_iter

    def classify(self, points):
        # distance
        classification = distances = {}
        for pt in range(len(points)):
            temp = []
            for center in self.centers:
                diff = abs(points.iloc[pt][0]-center[0]) + abs(points.iloc[pt]
                                                               [1]-center[1]) + abs(points.iloc[pt][2]-center[2])
                temp.append(diff)
            distances[pt] = temp

        # classifing
            centeroid = distances[pt].index(min(distances[pt]))
            classification[pt] = centeroid
        return classification

    def fit(self, data):
        points = pd.DataFrame(data)

        # intialize random centroids
        self.centers = random.sample(pts, k=self.k)
        print(self.centers)

        # optimize and print last optimized centroids
        self.optimize(points)
        print(self.centers)

        # classify according to last centeroids positions
        print(self.classify(points))

    def optimize(self, points):
        for i in range(self.max_iter):
            classification = self.classify(points)
            # get mean of each centroid
            centeroids = []
            for center in range(len(self.centers)):
                temp = []
                for pt in classification.keys():
                    if classification[pt] == center:
                        temp.append(pt)
            # #looping on one of the points to get the dimension
                centeroids.append([points.iloc[temp, i].mean(axis=0)
                                   for i in range(len(pts[0]))])
            if centeroids is self.centers:
                break
            else:
                self.centers = centeroids
        return

    def predict(self, data):
        return self.classify(data)


'''
# test
pts = [[.5, 4.5, 2.5], [2.2, 1.5, .1], [3.9, 3.5, 1.1], [2.1, 1.9, 4.9], [.5, 3.2, 1.2],
       [.8, 4.3, 2.6], [2.7, 1.1, 3.1], [2.5, 3.5, 2.8], [2.8, 3.9, 1.5], [.1, 4.1, 2.9]]

km = Kmeans(k=3)
km.fit(pts)
print('=============================')
print('prediction')
print(km.predict(pd.DataFrame(data=[[.5, 4, 3], [2.5, 4, 2.5]])))
'''
