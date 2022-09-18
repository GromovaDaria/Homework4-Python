# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#from cmath import pi
#
#d = int(input('Enter the precision of π: '))
#print(f'The number π with a given accuracy {d} is: {round(pi,d)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#num = int(input('Enter the number: '))
#i = 2
#list = []
#t = num
#while i <= num:
#    if num % i == 0:
#        list.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
#print(f'Prime factors of {t} are listed: {list}')

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#from random import randint
#
#def create_list(size, m, n):
#    return [randint(m, n) for i in range(size)]
#
#def get_unic_value(list):
#    return [i for i in set(list)]
#
#size = 5
#m = 1
#n = 5
#
#origin = create_list(size, m, n)
#print(origin)
#print(get_unic_value(origin))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#import itertools
#from random import randint
#
#k = int(input('Enter degree k: '))
#
#def random_numbers(k):
#    numbers = [randint(0,100) for i in range(k)]
#    while numbers[0] == 0:
#        numbers[0] = randint(1, 10) 
#    return numbers
#
#def x(k, numbers):
#    f = ['*x^']*(k-1) + ['*x']
#    lalala = [[a, b, c] for a, b, c in itertools.zip_longest(numbers, f, range(k, 1, -1), fillvalue= '') if a != 0]
#    for x in lalala:
#        x.append(' + ')
#    lalala = list(itertools.chain(*lalala))
#    lalala[-1] = ' = 0'
#    return "".join(map(str, lalala)).replace(' 1*x', ' x')
#numbers = random_numbers(k)
#check_list = x(k, numbers)
#print(check_list)
#
#with open('task4,1.txt', 'w') as data:
#    data.write(check_list)
#
#k = int(input('Enter the degree of the second polynomial: '))
#
#numbers = random_numbers(k)
#check_list2 = x(k,numbers)
#print(check_list2)
#
#with open('task4,2.txt', 'w') as data:
#    data.write(check_list2)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from itertools import chain
import itertools
import re

file1 = 'task4,1.txt'
file2 = 'task4,2.txt'
file_sum = 'sum.txt'

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:     
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)