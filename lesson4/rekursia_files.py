import os
import sys

# os.listdir(path) функция, которая показывает содержимое по указанному пути

path = sys.argv[1] #'C:\Users\Lenovo\Desktop\ОАК'    

def obxod_file(path, level=1):
    print('Level =', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.isdir(path+'\\' + i):
            print('Спускаемся', path+'\\' + i)
            obxod_file(path+'\\' + i, level + 1)
            print('Возвращаемся в', path)

obxod_file(path)
