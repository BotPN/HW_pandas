import pandas as pd
import numpy as np
import random
import string
from task_5 import df_st

product = input('Введите название товвара: ')

print(df_st[product])

market = input('Введите название магазина: ')
df_markets=df_st[df_st['Магазины'] == market]
print(df_markets)