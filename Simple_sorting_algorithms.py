import numpy as np  # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint  # імпортуємо функцію для генерування цілих випадкових чисел
import timeit  # імпортуємо модуль для обрахунку часу роботи функцій сортування
import copy  # імпортуємо біблотеку для створення глибокої копії

def Buble_sort(A, key='+'):
    ''' Бульбашкове сортування

    :param A: вихідний масив
    :param key: тип сортування (+ за зростанням, - за спаданням) за замовч.тип сортування - за зростанням
    :return: відсортований масив
    '''
    n, i = len(A), 0
    compr, exch = 0, 0  # вводимо змінні для обрахунку порівнянь (compr) та обмінів (exch)
    flag = True
    B = copy.deepcopy((A))  # створюємо глибоку копію масиву А, щоб не призводити до змін у вихідному масиві
    if key == '+':  # сортування за зростанням
        while flag:
            flag = False
            for j in range(n - i - 1):
                compr += 1
                if B[j] > B[j + 1]:
                    B[j], B[j + 1] = B[j + 1], B[j]
                    exch += 1
                    flag = True
            i += 1
    elif key == '-':  # сортування за спаданням
        while flag:
            flag = False
            for j in range(n - i - 1):
                compr += 1
                if B[j] < B[j + 1]:
                    B[j], B[j + 1] = B[j + 1], B[j]
                    exch += 1
                    flag = True
            i += 1
    return B, compr, exch  # функція повертає список ('відсортований масив', 'кільіксть порівнянь', 'кільіксть обмінів')

def Selection_sort(A, key='+'):
    ''' Сортування вибором

    :param A: вихідний масив
    :param key: тип сортування (+ за зростанням, - за спаданням) за замовч.тип сортування - за зростанням
    :return: відсортований масив
    '''
    n, i = len(A), 0
    B = copy.deepcopy((A))  # створюємо глибоку копію масиву А, щоб не призводити до змін у вихідному масиві
    compr, exch = 0, 0  # вводимо змінні для обрахунку порівнянь (compr) та обмінів (exch)
    if key == '+':  # сортування за зростанням
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                compr += 1
                if B[j] < B[min]:
                    min = j
            exch += 1
            B[i], B[min] = B[min], B[i]
    elif key == '-':  # сортування за спаданням
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                compr += 1
                if B[j] > B[min]:
                    min = j
            exch += 1
            B[i], B[min] = B[min], B[i]
    return B, compr, exch  # функція повертає список ('відсортований масив', 'кільіксть порівнянь', 'кільіксть обмінів')

def Insertion_sort(A, key='+'):
    ''' Сортування вставками

    :param A: вихідний масив
    :param key: тип сортування (+ за зростанням, - за спаданням) за замовч.тип сортування - за зростанням
    :return: відсортований масив
    '''
    n = len(A)
    B = copy.deepcopy(A)  # створюємо глибоку копію масиву А, щоб не призводити до змін у вихідному масиві
    compr, exch = 1, 0  # вводимо змінні для обрахунку порівнянь (compr) та обмінів (exch)
    if key == '+':  # сортування за зростанням
        for i in range(1, n):
            x = B[i]
            l, r = 0, i - 1
            while l <= r:
                compr += 2
                m = (l + r) // 2
                if x < B[m]:
                    r = m - 1
                else:
                    l = m + 1
            for j in range(i - 1, l - 1, -1):
                B[j + 1] = B[j]
                exch += 1
            B[l] = x
            exch += 1
    elif key == '-':  # сортування за спаданням
        for i in range(1, n):
            x = B[i]
            l, r = 0, i - 1
            while l <= r:
                compr += 2
                m = (l + r) // 2
                if x > B[m]:
                    r = m - 1
                else:
                    l = m + 1
            for j in range(i - 1, l - 1, -1):
                B[j + 1] = B[j]
                exch += 1
            B[l] = x
            exch += 1
    return B, compr, exch  # функція повертає список ('відсортований масив', 'кільіксть порівнянь', 'кількість обмінів')

while True:
    while True:  # перевірка на правильність введення даних
        quest = input('Do you want input the data (1) or choose random data (2) ')  # вибір введення даних з клавіатури чи заповнення масиву рандомними числами
        if quest == '1' or quest == '2':  # виклячення випадку, що користувач введе не 1 і не 2
            break
        else:
            print('Choose 1 or 2')
    if quest == '1':  # гілка для введення масиву вручну
        while True:  # перевірка на правильність введення даних
            try:
                n = int(input('Input the number of array elements (maximum 30): '))  # запитуємо кількість елементів
                if 0 < n <= 30:  # виключення випадку, що користувач введе число не в межах від 1 до 30
                    break
                else:
                    print('----The number does not satisfy the condition. Try again----')
            except ValueError:
                print('----It is not a number. Try again----')

        A = np.zeros(n, dtype=int)  # ініціалізуємо масив нулями кількості, яку задав користувач
        for i in range(n):
            while True:  # перевірка на правильність введення даних
                try:
                    A[i] = int(input(f'A{i} = '))   # циклічно заповнюємо масив
                    break
                except ValueError:
                    print('----It is not a number. Try again----')
        print(A, end='\n\n')
    elif quest == '2':  # гілка для заповнення масиву рандомними числами
        while True:  # перевірка на правильність введення даних
            try:
                n = int(input('How many numbers to generate: '))  # запитуємо скільки елементів згенерувати
                if n > 0:  # виключення випадку, що коритсувач введе від'ємне число
                    break
            except ValueError:
                print('It is not a number')
        A = np.zeros(n, dtype=int)  # ініціалізуємо масив нулями кількістю, який задав користувач
        for i in range(n):
            A[i] = randint(-n, n)  # циклічно заповнюємо масив рандомними числами

    test_1 = Buble_sort(A)  # сортування бульбашкою за зростанням
    print(f'Buble_sort(A) = {test_1[0]}, \ncomparisons = {test_1[1]}, exchanges = {test_1[2]}, \
time = {timeit.timeit("Buble_sort(A)", setup="from __main__ import Buble_sort, A", number=1)}', end='\n\n')

    test_2 = Selection_sort(A, '-')  # сортування вибором за спаданням
    print(f'Selection_sort(A) = {test_2[0]}, \ncomparisons = {test_2[1]}, exchanges = {test_2[2]}, \
time = {timeit.timeit("Selection_sort(A)", setup="from __main__ import Selection_sort, A", number=1)}', end='\n\n')

    test_3 = Insertion_sort(A)  # сортування вставками за зростанням
    print(f'Insertion_sort(A) = {test_3[0]}, \ncomparisons = {test_3[1]}, exchanges = {test_3[2]}, \
time = {timeit.timeit("Insertion_sort(A)", setup="from __main__ import Insertion_sort, A", number=1)}', end='\n\n')

    # запитуємо кристувача чи продовжувати роботу далі, чи завершити програму
    answer = input('Do you want to continue (+) or complete the program (anything)? ')
    if answer == '+':
        continue
    else:
        break
