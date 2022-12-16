#Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов

#import random

#print('Ввидите длинну списка (число)')
#n = int(input())

#list = [random.uniform(1, 100) for i in range(n)]
#print(f'Сгенерированный список {list}')

#new_list = [i % 1 for i in list if i % 1 != 0]
#print(max(new_list) - min(new_list))

import random

print('Ввидите длинну списка (число)')
n = int(input())

my_list = [random.uniform(1, 100) for i in range(n)]
print(f'Сгенерированный список {my_list}')

new_list = list(map(lambda number: number % 1, my_list))
print(max(new_list) - min(new_list))