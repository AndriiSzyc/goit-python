# import os
# import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
# path = sys.argv[1]

path = ['Выписка.PDF', 'довідка з банку про відкритий рахунок (1).pdf',
'Довідка СТАТИСТИКА.pdf', 'Лист ДПІ.pdf', 'НАКАЗ № 1.pdf',
'ПДВ.pdf', 'Перечень правоустанавливающих документов.docx',
'ФУМ ДЕЗ СтаПІ.pdf', 'НАКАЗ № 1.pdf', 'ПДВ.pdf', 'Перечень пртут (1).pdf',
'131825465_836372503807091_3249100478024097785_n.jpg',
'dmitrij-shostakovich-simfoniya-4-do-minor-soch.-43_(mp3CC.biz).mp3']

#print(f"Start in {path}")

# files - это список имен файлов и папок в path.
# files = os.listdir(path)
# print(files)

files = path.copy() # files - class 'list'
#print(files)


print(f'В папке {len(files)} документов\n') # количество элементов

#str_files = ' '.join(files) # из списка в строку
#print(str_files)

#unique_files = set(files) # уникальные символы
#print(unique_files)



elements_dict = {} # создаем пустой словарь
for elements in files: # разбиваем список строк на ключ - значение 
    elements_dict[elements] = elements.split('.')[-1].upper()
print(elements_dict)

extention = elements_dict.values() # вычленяем значения словаря, они же расширение файла
extention = set(extention) # множество из значений расширений
print(f'Have a next extentions: {list(extention)}\n')


empty_list_picture = []
empty_list_video = []
empty_list_doc = []
empty_list_music = []
empty_list_unknown = []

for i in files:
    if i.split('.')[-1].upper()== 'PDF': #or 'DOC' or 'DOCX' or 'TXT':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'DOC':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'DOCX':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'TXT':
        empty_list_doc.append(i)
        
    elif i.split('.')[-1].upper()== 'JPG': #'JPEG' or 'PNG' or :
        empty_list_picture.append(i)
    elif i.split('.')[-1].upper()== 'JPEG':
        empty_list_picture.append(i)
    elif i.split('.')[-1].upper()== 'PNG':
        empty_list_picture.append(i)
        

    elif i.split('.')[-1].upper()== 'MP3':
        empty_list_music.append(i)
    elif i.split('.')[-1].upper()== 'OGG':
        empty_list_music.append(i)
    elif i.split('.')[-1].upper()== 'WAV':
        empty_list_music.append(i)    
    elif i.split('.')[-1].upper()== 'AMR':
        empty_list_music.append(i)

    elif i.split('.')[-1].upper()== 'AVI':
        empty_list_video.append(i)
    elif i.split('.')[-1].upper()== 'MP4':
        empty_list_video.append(i)
    elif i.split('.')[-1].upper()== 'MOV':
        empty_list_video.append(i)
    else:
        empty_list_unknown.append(i)

print(f'Contains documents:\n{empty_list_doc}\n')
print(f'Contains pictures:\n{empty_list_picture}\n')
print(f'Contains videos:\n{empty_list_video}\n')
print(f'Contains musiks:\n{empty_list_music}\n')    
print(f'Contains unknown files:\n{empty_list_unknown}\n')

#  C:/python/sort.py C:/Users/Lenovo/Desktop/Документы

