# четных чисел 507

import pandas as pd

# импортирую данные из файла ексель
df = pd.read_excel(
    "task_support.xlsx",
    sheet_name="Tasks",
    header=1,
    usecols="B"
)

# конвертирую PandasDataFrame в list
dflist = df.values.tolist()

# задаю переменную для подсчета
count = 0

# прохожу циклом по списку и проверяю на четность каждый элемент
# если нахожу четный плюсую счетчик
for num in dflist:
    num = num[0]
    if num % 2 == 0:
        count += 1

print(count)
