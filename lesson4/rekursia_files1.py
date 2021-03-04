# Рекурсивный обход файлов

import os # Модуль предоставляет функций для работы
#         с операционной системой

import sys

# os.listdir(path) функция, которая показывает
#                содержимое по указанному пути

path = sys.argv[1] #'C:\Users\Lenovo\Desktop\ОАК'    
#print('Type path',os.listdir(path))

spisok = []

def obxod_file(path, level=1):
    #print('Level =', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        #print(i, type(i))
        if i.rfind('.') > -1:
            spisok.append(i)

    for i in os.listdir(path):
        if os.path.isdir(path+'\\' + i): # проверяет папка или нет
            #print('Спускаемся', path+'\\' + i)
            obxod_file(path+'\\' + i, level + 1)
            #print('Возвращаемся в', path)

obxod_file(path)

#print(spisok, len(spisok))

elements_dict = {} # пустой словарь

for elements in spisok: 
    elements_dict[elements] = elements.split('.')[-1].upper() # заполняем список

extention = elements_dict.values() # вычленяем значения словаря
extention = set(extention) # множество из значений
print(f'Have a next extentions: {list(extention)}\n')    

empty_list_picture = []
empty_list_video = []
empty_list_doc = []
empty_list_music = []
empty_list_arkhiv = []
empty_list_unknown = []


for i in spisok:
    if i.split('.')[-1].upper()== 'PDF': 
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'DOC':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'DOCX':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'TXT':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'XLSF':
        empty_list_doc.append(i)
    elif i.split('.')[-1].upper()== 'PPTX':
        empty_list_doc.append(i)    
        
        
    elif i.split('.')[-1].upper()== 'JPG': 
        empty_list_picture.append(i)
    elif i.split('.')[-1].upper()== 'JPEG':
        empty_list_picture.append(i)
    elif i.split('.')[-1].upper()== 'PNG':
        empty_list_picture.append(i)
    elif i.split('.')[-1].upper()== 'SVG':
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
    elif i.split('.')[-1].upper()== 'MKV':
        empty_list_video.append(i)

    elif i.split('.')[-1].upper()== 'ZIP':
        empty_list_arkhiv = []
    elif i.split('.')[-1].upper()== 'GZ':
        empty_list_arkhiv = []
    elif i.split('.')[-1].upper()== 'TAR':
        empty_list_arkhiv = []
    else:
        empty_list_unknown.append(i)

        
print(f'Contains documents:\n{empty_list_doc}\n')
print(f'Contains pictures:\n{empty_list_picture}\n')
print(f'Contains videos:\n{empty_list_video}\n')
print(f'Contains musiks:\n{empty_list_music}\n')    
print(f'Contains arkhiv:\n{empty_list_arkhiv}\n')
print(f'Contains unknown files:\n{empty_list_unknown}\n')

unknown_elements_dict = {} # пустой словарь

for elements in empty_list_unknown: 
    unknown_elements_dict[elements] = elements.split('.')[-1].upper() # заполняем список

extention_unknown = unknown_elements_dict.values() # вычленяем значения словаря
extention_unknown = set(extention_unknown) # множество из значений
print(f'Have a next unknown extentions: {list(extention_unknown)}\n')   

# os.path.isfile(path+'\\' + i) проверяет является ли элемент фаойлом

#  C:/python/rekursia_files1.py C:/Users/Lenovo/Desktop/ОАК
