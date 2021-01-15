import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)
#print(files)
print(f'в папке {len(files)} документов')

elements_dict = {} # пустой список

for elements in files: 
    elements_dict[elements] = elements.split('.')[-1].upper() # заполняем список
    
#print(elements_dict)

extention = elements_dict.values() # вычленяем значения словаря
extention = set(extention) # множество из значений
print(f'Have a next extentions: {list(extention)}')

