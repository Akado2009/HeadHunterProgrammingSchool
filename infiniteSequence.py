import argparse
import re

#### Генерирование последовательности до заданного числа включительно
#### input_number - заданное число
def getSequence(input_number):
	number = ""
	for i in range(input_number + 1):
		number += "%i" %i
	return number


#### Получение индекса числа
#### input_number - заданное число
def getIndex(input_number):
	number = str(input_number)
	infiniteSequence = getSequence(input_number)
	m = re.search(number, infiniteSequence)
	q = m.span()[0]
	del infiniteSequence
	return q

#### Парсинг файла с числами (если таковой имеется)
#### filename - имя файла
def parseFile(filename):
	fileOpened = open(filename, "r")
	numbers = [int(line.strip().split(" ")) for line in fileOpened]
	if (len(numbers) == 0):
		numbers = [int(line.strip().split("\t")) for line in fileOpened]
		if (len(numbers) == 0):
			numbers = [int(line.strip().split(",")) for line in fileOpened]
			if (len(numbers) == 0):
				print("Incorrect file format")
				return;
	return numbers

#### Парсер аргументов командной строки
def parser():
	parser = argparse.ArgumentParser(description = "Finding the number in infinite sequence of integers fused together.")
	subparsers = parser.add_subparsers(help='sub-command help')
	parser_number = subparsers.add_parser('n',  help = "The number to be found.")
	parser_number.add_argument("number", type = int, nargs='+')
	parser_file = subparsers.add_parser('f',  help = "File containing the number.")
	parser_file.add_argument("file", type = str)
	argumentInput = str(parser.parse_args()).split("=")[1].strip(")")
	if "." in argumentInput:
		filename = argumentInput.strip("'")
		massiveOfNumbers = parseFile(filename)
		return massiveOfNumbers
	else:
		listOfNumbers = [int(s) for s in argumentInput.strip("]").strip("[").split(',')]
		return listOfNumbers

#### Главная функция
def mainPart():
	numbers = parser()
	indexes = list(map(getIndex,numbers))
	indexes = [str(i) for i in indexes]
	print('\n'.join(indexes))


if __name__ == "__main__":
	mainPart()
