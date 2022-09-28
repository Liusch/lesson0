import os
import pandas as pd
import time

path = input('Введите директорию. Например "C:\\Games" ')
listFiles = []
listDirectory = []
listDirectorySlash = []
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

readDir(path)

for value in listDirectory:
    value = value.replace('\\', '/')
    listDirectorySlash.append(value)

print(listDirectorySlash)
print('Список всех файлов: ', listFiles)
df = pd.DataFrame(listFiles, columns=['Список файлов'])
df.to_excel('./result.xlsx')