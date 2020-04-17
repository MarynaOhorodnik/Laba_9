import numpy as np  # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint  # імпортуємо функцію для генерування цілих випадкових чисел
import timeit  # імпортуємо модуль для обрахунку часу роботи функцій сортування
import copy  # імпортуємо біблотеку для створення глибокої копії

def Coctail_Sort(A, key = '+'):
    ''' Сортування перемішуванням

    :param A: вихідний масив
    :param key: тип сортування (+ за зростанням, - за спаданням) за замовч.тип сортування - за зростанням
    :return: відсортований масив
    '''
    B = copy.deepcopy(A)  # створюємо глибоку копію масиву А, щоб не призводити до змін у вихідному масиві
    n = len(B)
    flag = True
    start, end = 0, n - 1
    compr, exch = 0, 0  # вводимо змінні для обрахунку порівнянь (compr) та обмінів (exch)
    if key == '+':  # сортування за зростанням
        while flag:
            flag = False
            for i in range(start, end):
                compr += 1
                if B[i] > B[i + 1]:
                    exch += 1
                    B[i], B[i + 1] = B[i + 1], B[i]
                    flag = True
            if flag == False:
                break
            flag = False
            end = end - 1
            for j in range(end - 1, start - 1, -1):
                compr += 1
                if B[j] > B[j + 1]:
                    exch += 1
                    B[j], B[j + 1] = B[j + 1], B[j]
                    flag = True
            start = start + 1
    elif key == '-':  # сортування за спаданням
        while flag:
            flag = False
            for i in range(start, end):
                compr += 1
                if B[i] < B[i + 1]:
                    exch += 1
                    B[i], B[i + 1] = B[i + 1], B[i]
                    flag = True
            if flag == False:
                break
            flag = False
            end = end - 1
            for j in range(end - 1, start - 1, -1):
                compr += 1
                if B[j] < B[j + 1]:
                    exch += 1
                    B[j], B[j + 1] = B[j + 1], B[j]
                    flag = True
            start = start + 1
    return B, compr, exch  # функція повертає список ('відсортований масив', 'кільіксть порівнянь', 'кількість обмінів')

def Shell_Sort(A, key = '+'):
    ''' Сортування Шелла

    :param A: вихідний масив
    :param key: тип сортування (+ за зростанням, - за спаданням) за замовч.тип сортування - за зростанням
    :return: відсортований масив
    '''
    B = copy.deepcopy(A)  # створюємо глибоку копію масиву А, щоб не призводити до змін у вихідному масиві
    n = len(B)
    compr, exch = 0, 0  # вводимо змінні для обрахунку порівнянь (compr) та обмінів (exch)
    gap = n // 2
    if key == '+':  # сортування з азростанням
        while gap > 0:
            for i in range(gap, n):
                temp = B[i]
                j = i
                while j >= gap and B[j - gap] > temp:
                    compr += 1
                    exch += 1
                    B[j] = B[j - gap]
                    j -= gap
                exch += 1
                B[j] = temp
            gap //= 2
    elif key == '-':  # сортування за спаданням
        while gap > 0:
            for i in range(gap, n):
                temp = B[i]
                j = i
                while j >= gap and B[j - gap] < temp:
                    compr += 1
                    exch += 1
                    B[j] = B[j - gap]
                    j -= gap
                compr += 1
                exch += 1
                B[j] = temp
            gap //= 2
    return B, compr, exch  # функція повертає список ('відсортований масив', 'кільіксть порівнянь', 'кількість обмінів')

def Heap_Sort(A, key = '+'):
    ''' Пірамідальне сортування

    :param A: вихідний масив
    :param key: тип сортування (+ за зростанням, - за спаданням) за замовч.тип сортування - за зростанням
    :return: відсортований масив
    '''
    B = copy.deepcopy(A)  # створюємо глибоку копію масиву А, щоб не призводити до змін у вихідному масиві
    n = len(B)
    compr, exch = 0, 0  # вводимо змінні для обрахунку порівнянь (compr) та обмінів (exch)
    for i in range(n // 2 - 1, -1, -1):
        h = heapify(B, n, i, key, compr, exch)
        compr, exch = h[0], h[1]

    for j in range(n - 1, 0, -1):
        B[j], B[0] = B[0], B[j]
        h = heapify(B, j, 0, key, compr, exch)
        compr, exch = h[0], h[1]
    return B, compr, exch  # функція повертає список ('відсортований масив', 'кільіксть порівнянь', 'кількість обмінів')

def heapify(B, n, i, key, compr, exch):
    ''' Функція, яка перетворює масив у сортувальне дерево та переміщує максимальні чи мінімальні елементи по порядку
    в кінець списку

    :param B: вихідний масив
    :param n: довжина вихідного масиву
    :param i: індекс ітерації, який передається з циклу функції сортування
    :param key: тип сортування (+ за зростанням, - за спаданням)
    :param compr: змінна-лічильник, яка обраховує кількість порівнянь
    :param exch: змінна-лічильник, яка обраховує кількість обмінів
    :return: compr та exch, щоб зберегти дані за весь процес сортування
    '''
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if key == '+':  # сортування за зростанням
        compr += 1
        if l < n and B[i] < B[l]:
            largest = l

        compr += 1
        if r < n and B[largest] < B[r]:
            largest = r

        if largest != i:
            exch += 1
            B[i], B[largest] = B[largest], B[i]
            h = heapify(B, n, largest, key, compr, exch)
            compr, exch = h[0], h[1]
    elif key == '-':  # сортування за спаданням
        compr += 1
        if l < n and B[i] > B[l]:
            largest = l

        compr += 1
        if r < n and B[largest] > B[r]:
            largest = r

        if largest != i:
            exch += 1
            B[i], B[largest] = B[largest], B[i]
            h = heapify(B, n, largest, key, compr, exch)
            compr, exch = h[0], h[1]
    return compr, exch  # функція повертає список ('кільіксть порівнянь', 'кількість обмінів')


while True:
    while True:  # перевірка на правильність введення даних
        try:
            n = int(input('How many numbers to generate: '))  # запитуємо скільки елементів згенерувати
            if n > 0:  # виключення випадку, що коритсувач введе від'ємне число
                break
            else:
                print('Input a positive number')
        except ValueError:
            print('It is not a number. Try again')
    A = np.zeros(n, dtype=int)  # ініціалізуємо масив нулями кількістю, який задав користувач
    for i in range(n):
        A[i] = randint(-n, n)  # циклічно заповнюємо масив рандомними числами

    while True:
        while True:
            try:  # вибір типу сортування
                quest_1 = int(input('Choose the sort type: Coctail sort (1), Shell sort (2), Heap sort (3): '))
                if quest_1 in range(1, 4):
                    break
                else:
                    print('Input (1) or (2) or (3)')
            except ValueError:
                print('It is not a number. Try again')
        while True:
            quest_2 = input('Sort by ascending (+) or by descending (-)? ')
            if quest_2 == '+' or quest_2 == '-':
                break
            else:
                print('Input + or -')

        if quest_1 == 1:
            test_1 = Coctail_Sort(A, quest_2)
            print(f'Coctail_sort(A) = {test_1[0]}, \ncomparisons = {test_1[1]}, exchanges = {test_1[2]}, '
                  f'time = {timeit.timeit("Coctail_Sort(A)", setup="from __main__ import Coctail_Sort, A", number=1)}')
        elif quest_1 == 2:
            test_2 = Shell_Sort(A, quest_2)
            print(f'Shell_sort(A) = {test_2[0]}, \ncomparisons = {test_2[1]}, exchanges = {test_2[2]}, '
                  f'time = {timeit.timeit("Shell_Sort(A)", setup="from __main__ import Shell_Sort, A", number=1)}')
        elif quest_1 == 3:
            test_3 = Heap_Sort(A, quest_2)
            print(f'Heap_sort(A) = {test_3[0]}, \ncomparisons = {test_3[1]}, exchanges = {test_3[2]}, '
                  f'time = {timeit.timeit("Heap_Sort(A)", setup="from __main__ import Heap_Sort, A", number=1)}')

        answer = input('Do you want to choose other sort type (1) or generate a new array (2) or finish the program (anything): ')
        if answer == '1':
            continue
        else:
            break

    if answer == '2':
        continue
    else:
        break
