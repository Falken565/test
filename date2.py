# всего 138 вторников

import pandas as pd

import datetime as dt

# импортирую данные из файла ексель
df = pd.read_excel(
    "task_support.xlsx",
    sheet_name="Tasks",
    header=1,
    usecols="F"
)

# конвертирую PandasDataFrame в list
dflist = df.values.tolist()


# функция для получения дня недели
def parse_to_day(n):
    parsedate = n.split(" ")
    d = dt.datetime.strptime(parsedate[0], '%Y-%m-%d')
    day = d.isoweekday()
    return day


# задаю переменную для подсчета
count = 0

# прохожу циклом по списку и проверяю каждый элемент
# если нахожу где день вторник плюсую счетчик
for date in dflist:
    date = date[0]
    if parse_to_day(date) == 2:
        count += 1

print(count)
