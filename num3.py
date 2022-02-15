# чисел меньше 0.5 всего 485 чисел

import pandas as pd

# импортирую данные из файла ексель
df = pd.read_excel(
    "task_support.xlsx",
    sheet_name="Tasks",
    header=1,
    usecols="D"
)

# конвертирую PandasDataFrame в list
dflist = df.values.tolist()


# функция для приведения полученного значения к типу float
def parse_to_float(n):
    nospace = n.replace(" ", "")
    truefloat = nospace.replace(",", ".")
    return float(truefloat)


# задаю переменную для подсчета
count = 0

# прохожу циклом по списку и проверяю каждый элемент
# если нахожу < 0.5 плюсую счетчик
for num in dflist:
    num = num[0]
    if parse_to_float(num) < 0.5:
        count += 1

print(count)
