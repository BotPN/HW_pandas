''' Напишите программу, которая:
 - Генерирует случайые данные о ежедневных объемах продаж ноутбуков,
 планшетов и смартфонов в магазинах A,B,C,D,E,..., X,Y,Z.
 - Выведите описательные статистики по товарам и по магазинам'''

import pandas as pd
import numpy as np
import random
import string

list_ABC = [i for i in string.ascii_uppercase]

df_st=pd.DataFrame({
    'Магазины': list_ABC,
    'Ноутбуки': [random.randint(0,850000) for i in range(len(list_ABC))],
    'Планшеты': [random.randint(0,100000) for i in range(len(list_ABC))],
    'Смартфоны': [random.randint(0,1000000) for i in range(len(list_ABC))]
 })

print(f'Описательная статистика по товарам: \n {df_st.describe()}\n')

markets = df_st['Магазины'].describe()
print(f'Описательная статистика по магазинам: \n {markets}\n')