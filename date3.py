# ответ 40

import pandas as pd

import datetime as dt


# импортирую данные из файла ексель
df = pd.read_excel(
    "task_support.xlsx",
    sheet_name="Tasks",
    header=1,
    usecols="G"
)

# конвертирую PandasDataFrame в list
dflist = df.values.tolist()


# функция для получения дня недели
def last_tue(n):
    # определяем день недели и месяц
    currentdate = dt.datetime.strptime(n, '%m-%d-%Y')
    currentcalendar = currentdate.timetuple()
    currentday = currentcalendar[6]
    currentmonth = currentcalendar[1]
    # определяем месяц через неделю (7 дней)
    week = dt.timedelta(days=7)
    date = currentdate + week
    calendar = date.timetuple()
    month = calendar[1]
    # проверяем, что следующий вторник не находится в текущем месяце
    if currentday == 1 and month > currentmonth:
        return True
    return False


# задаю переменную для подсчета
count = 0

# прохожу циклом по списку и проверяю каждый элемент
# если функция утверждает, что вторник последний плюсую счетчик
for date in dflist:
    date = date[0]
    if last_tue(date):
        count += 1

print(count)
