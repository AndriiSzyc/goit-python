elements_dict = {} # пустой словарь

def unique_extensions(some_spisok, some_elements_dict):
    for elements in some_spisok: 
        some_elements_dict[elements] = elements.split('.')[-1].upper() # заполняем список

    extention = some_elements_dict.values() # вычленяем значения словаря
    extention = set(extention) # множество из значений
    print(f'Have a next extentions: {list(extention)}\n')    
