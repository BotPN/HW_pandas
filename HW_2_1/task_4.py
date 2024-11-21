'''Для DataFrame из предыдущей задачи отсортируйте данные по размеру зарплаты. Из отсортированного DataFrame 
выведите 5 первых строк и  последних'''


import pandas as pd
import numpy as np
import random
from task_3 import df_staff 

df_sorted = df_staff.sort_values('Зарплата')

print(f'{df_sorted[:5]} \n {df_sorted[-3:]}')
