import pandas as pd

# Для начала необходимо считать таблицу
df = pd.read_csv('dz.csv')

# Средняя ЗП в зависимость от города проживания
moscow_salary = df[df['City'] == 'Москва']['Salary'].mean()
print(f"Средняя зарплата в Москве: {moscow_salary}")

group = df.groupby('City')['Salary'].mean()
print(group)