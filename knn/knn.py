from numpy import *
import operator

def createDataSet():
    group = array([[0, 0, 0], [0.1, 0, 0.9], [0.9, 0.1, 0], [0, 0.1, 0.9],
                   [0.1, 0.1, 0.1], [0.4, 0.4, 0.4], [0.1, 0.1, 0.4], [0.4, 0.4, 0.1],
                   [0.6, 0.4, 0.4], [0.4, 0.6, 0.4], [0.4, 0.4, 0.6], [0.9, 0.4, 0.4],
                   [0.6, 0.6, 0.4], [0.6, 0.4, 0.6], [0.6, 0.1, 0.6], [0.1, 0.6, 0.6],
                   [0.6, 0.6, 0.6], [0.9, 0.6, 0.6], [0.6, 0.9, 0.6], [0.9, 0.6, 0.9],
                   [1, 0, 0], [0.1, 0, 1], [0, 1, 0], [1, 1, 1],
                   ])
    labels = ['A', 'A', 'A', 'A',
              'B', 'B', 'B', 'B',
              'C', 'C', 'C', 'C',
              'D',  'D', 'D', 'D',
              'E', 'E', 'E', 'E',
              'S', 'S', 'S', 'S',]
    return group, labels
def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    clasCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        clasCount[voteIlabel] = clasCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(clasCount.iteritems(),
    key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
label = classify([0.5, 0.5, 0.5], group, labels, 3)
print label
