import argparse
from math import *

#### подсчет радиуса, как минимального расстояния до точки, исключая расстояние "до себя"
#### array - матрица расстояний
def calculateRadiuses(array):
	radiuses = []
	for i in range(len(array)):
		tmp = array[i]
		del tmp[i]
		radiuses.append(min(tmp))
	return radiuses

#### нахождение кол-ва соседей (точек, лежащих в пределах двойного радиуса)
#### r - радиус, array - матрица расстояний
def findBelowRadius(r, array):
	count = 0
	for i in range(len(array)):
		if 2*r >= array[i]:
			count += 1
	return count

#### построение матрицы расстояний
#### x,y - массив координат точек
def getDistanceMatrix(x,y):
	distanceMatrix = [[0 for i in range(len(x))]for j in range(len(x))]
	for i in range(len(x)):
		for j in range(len(x)):
			distanceMatrix[i][j] = calculateDistance(x[i], y[i], x[j], y[j])
	return distanceMatrix

#### функция подсчет эвклидова расстояния
#### x1, y1 - первая точка, x2, y2 - вторая
def calculateDistance(x1, y1, x2, y2):
	return sqrt((x1 - x2)**2 + (y1 - y2)**2)

#### парсинг ввода из командной строки
def parseInput():
	x = []
	y = []
	isInput = True
	while isInput:
		n = input()
		if n:
			x.append(int(n.split(" ")[0]))
			y.append(int(n.split(" ")[1]))
		else:
			isInput = False
	return x,y


#### парсинг ввода из файла
def parseFile(filename, sep = "\t"):
	x = []
	y = []
	parsingFile = open(filename, "r")
	for line in parsingFile:
		x.append(int(line.split(sep)[0]))
		y.append(int(line.split(sep)[1].strip()))
	return x,y

#### вывод результата
#### r - массив радиусов, counts - массив соседей
def getOutput(r, counts):
	for i in range(len(r)):
		print(str(int(r[i])) + " " + str(counts[i]))

#### главная функция
def mainPart():
	typeOfInput = input("Do you want to input manually (I) or use file instead (F) ? ")
	if str(typeOfInput) == "I":
		x,y = parseInput()
	elif str(typeOfInput) == "F":
		filename = input("Enter a file name: ")
		sep = input("Enter a separator: ")
		x, y = parsingFile(filename, sep)
	matrix = getDistanceMatrix(x,y)
	radiuses = calculateRadiuses(matrix)
	counts = [0 for i in range(len(radiuses))]
	for i in range(len(counts)):
		counts[i] = findBelowRadius(radiuses[i], matrix[i])
	getOutput(radiuses, counts)

if __name__ == "__main__":
	mainPart()
