import csv
import numpy as np
import math


def loadData(path):
    f = open(path, "r")
    data = csv.reader(f)
    data = np.array(list(data))
    data = np.delete(data, 0, 0)
    data = np.delete(data, 0, 1)
    np.random.shuffle(data)
    f.close()
    trainSet = data[:100]
    testSet = data[100:]
    return trainSet, testSet


def calcDistancs(pointA, pointB, numOfFeature=4):
    tmp = 0
    for i in range(numOfFeature):
        tmp += (float(pointA[i]) - float(pointB[i])) ** 2
    return math.sqrt(tmp)


def kNearestNeighbor(trainSet, point, k):
    distances = []
    for item in trainSet:
        distances.append({
            "label": item[-1],
            "value": calcDistancs(item, point)
        })
    distances.sort(key=lambda x: x["value"])
    labels = [item["label"] for item in distances]
    return labels[:k]


def findMostOccur(arr):
    labels = set(arr)
    ans = ""
    maxOccur = 0
    for label in labels:
        num = arr.count(label)
        if num > maxOccur:
            maxOccur = num
            ans = label
    return ans


if __name__ == "__main__":

    trainSet, testSet = loadData("/content/drive/MyDrive/xstk/xstk-KNN-main/Iris.csv")

    sepal_length = float(input("Nhập Sepal Length: "))
    sepal_width = float(input("Nhập Sepal Width: "))
    petal_length = float(input("Nhập Petal Length: "))
    petal_width = float(input("Nhập Petal Width: "))


    new_data_point = [sepal_length, sepal_width, petal_length, petal_width]

    k = 5 
    knn = kNearestNeighbor(trainSet, new_data_point, k)
    predicted_species = findMostOccur(knn)


    print("Dự đoán tên loài hoa: ", predicted_species)