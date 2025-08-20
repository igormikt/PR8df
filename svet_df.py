import pandas as pd

df = pd.read_csv('svetv2i.csv')

# Вывод первых 5 строк данных
print(df.head())

# Вывод информации о данных
print(df.info())

# Вывод статистического описания
print(df.describe())
