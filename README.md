# HeadHunterProgrammingSchool


###Задача 1.
Файл 2dPoints.py.
Допустимый ввод:
* Подряд с командную строку координаты через пробел:
  2 0
  2 3
  3 1
* Файл такого же вида.

Решение задачи осуществляется с помощью двумерное матрицы расстояний, где элемент с индексами **i**, **j** соответствует расстоянию от точки **xi** до **xj**. Меньшее значение в строке - **радиус** точки. Затем просто поиск количества точек с расстоянием меньших двойного радиуса точки.


###Задача 2.
Файл infiniteSequence.py.
Допустимый ввод через параметры командой строки:
* Запуск с параметром n:
  *py infiniteSequence.py n [numbers]*, где **numbers** - числа через пробел
* Запуск с параметром f:
  *py infiniteSequence.py f [filename]*, где **filename** - имя файла формата чисел идущих через запятую, табуляцию или пробел.

Решение задачи осуществяется с помощью поиска через регулярное выражение в строке, состоящей из чисел, слитиых вместе.  Для числа создается строка, содержащая все числа до него включительно (т.к. оно точно найдется в этой строке, если не раньше, то на своем месте в последвательности). И далее выполняется поиск с помощью регулярного выражения.
