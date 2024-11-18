''' В предыдущей задаче найдите среднией объем продаж выбранного товара. 
Выведите DataFrame с магазинами, объем продаж этого товара в которых был выше среднего'''

import pandas as pd
import numpy as np
import random
import string
from task_5 import df_st

product = input('Введите название товвара: ')

print(f'Средний объем продаж раздела {product} равен {df_st[product].mean()} \n')

df_markets=df_st[df_st[product] > df_st[product].mean()]

print(f'Магазины объем продаж выше среднего \n {df_markets}')
