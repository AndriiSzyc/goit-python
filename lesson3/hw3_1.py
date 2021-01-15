# import os
# import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
# path = sys.argv[1]

path = ['Выписка.PDF', 'довідка з банку про відкритий рахунок (1).pdf',
'Довідка СТАТИСТИКА.pdf', 'Лист ДПІ.pdf', 'НАКАЗ № 1.pdf',
'ПДВ.pdf', 'Перечень правоустанавливающих документов.docx',
'ФУМ ДЕЗ СтаПІ.pdf', 'НАКАЗ № 1.pdf', 'ПДВ.pdf', 'Перечень пртут (1).pdf']

#print(f"Start in {path}")

# files - это список имен файлов и папок в path.
# files = os.listdir(path)
# print(files)

files = path.copy() # files - class 'list'
#print(files)




set_extention_picture = ('JPEG', 'PNG', 'JPG')
set_extention_video = ('AVI', 'MP4', 'MOV')
set_extention_doc = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX')
set_extention_music = ('MP3', 'OGG', 'WAV', 'AMR')
set_unknown =(None)

print(f'В папке {len(files)} документов') # количество элементов

#str_files = ' '.join(files) # из списка в строку
#print(str_files)

#unique_files = set(files) # уникальные символы
#print(unique_files)



elements_dict = {} # создаем пустой словарь
for elements in files: # разбиваем список строк на ключ - значение 
    elements_dict[elements] = elements.split('.')[-1].upper()
#print(elements_dict)


extention = elements_dict.values() # вычленяем значения словаря, они же расширение файла
extention = set(extention) # множество из значений расширений
print(f'Have a next extentions: {list(extention)}')

list_extention_doc = []

dict_files = {('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX'): '',}
#print(dict_files)



#  C:/python/sort.py C:/Users/Lenovo/Desktop/Документы

