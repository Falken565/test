# простых числе 168

import pandas as pd

# импортирую данные из файла ексель
df = pd.read_excel(
    "task_support.xlsx",
    sheet_name="Tasks",
    header=1,
    usecols="C"
)

# конвертирую PandasDataFrame в list
dflist = df.values.tolist()


# функция проверки простого числа (взял из урока с курсов)
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


# задаю переменную для подсчета
count = 0

# прохожу циклом по списку и проверяю каждый элемент
# если нахожу простое число плюсую счетчик
for num in dflist:
    num = num[0]
    if is_prime(num):
        count += 1

print(count)
