import os
import pandas as pd
import time

path = input('Введите директорию. Например "C:\\Games" ')
listFiles = []
listDirectory = []
listDirectorySlash = []
timeCreatFile = []
timeLastModified = []
def readDir(path,level=1):
    print('Level =', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            readDir(path + '\\' + i, level+1)
            print('Возвращаемся в', path)
        elif os.path.isfile(path + '\\' + i):
            listFiles.append(i)
            listDirectory.append(path)

            ti_c = os.path.getctime(path + '\\' + i)
            c_ti = time.ctime(ti_c)
            ct_obj = time.strptime(c_ti)
            creatTime = time.strftime("%Y-%m-%d", ct_obj)
            timeCreatFile.append(creatTime)

            ti_m = os.path.getmtime(path + '\\' + i)
            m_ti = time.ctime(ti_m)
            mt_obj = time.strptime(m_ti)
            modifTime = time.strftime("%Y-%m-%d", mt_obj)
            timeLastModified.append(modifTime)

readDir(path)

for value in listDirectory:
    value = value.replace('\\', '/')
    listDirectorySlash.append(value)

unionList = list(zip(listFiles, listDirectorySlash, timeCreatFile, timeLastModified))

print(listDirectorySlash)
print('Список всех файлов: ', listFiles)
print(unionList)
print(timeCreatFile)
print(timeLastModified)
df = pd.DataFrame(unionList,
                  columns=['Имя файла', 'Директория', 'Дата создания файла', 'Дата изменения файла'],
                  index=range(1, (len(unionList) + 1)))
df.to_excel('./result.xlsx')

import openpyxl

def example():
    filename = "./result.xlsx"
    book = openpyxl.load_workbook(filename)
    sheet = book.active
    sheet.column_dimensions["A"].width = 10
    sheet.column_dimensions["B"].width = 40
    sheet.column_dimensions["C"].width = 40
    sheet.column_dimensions["D"].width = 25
    sheet.column_dimensions["E"].width = 25

    sheet.auto_filter.ref = "A1:E1"
    book.save(filename)

example()