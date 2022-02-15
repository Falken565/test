# всего 156 вторников

import pandas as pd

# импортирую данные из файла ексель
df = pd.read_excel(
    "task_support.xlsx",
    sheet_name="Tasks",
    header=1,
    usecols="E"
)

# конвертирую PandasDataFrame в list
dflist = df.values.tolist()


# функция для получения дня недели
def parse_to_day(date):
    parsedate = date.split(" ")
    return parsedate[0]


# задаю переменную для подсчета
count = 0

# прохожу циклом по списку и проверяю каждый элемент
# если нахожу где день вторник плюсую счетчик
for date in dflist:
    date = date[0]
    if parse_to_day(date) == "Tue":
        count += 1

print(count)
