input_string = input('Input sometsing ')


def normalize(sum_string):
    capital_letters = {ord('А'): 'A',
                   ord('Б'): 'B',
                   ord('В'): 'V',
                   ord('Г'): 'G',
                   ord('Д'): 'D',
                   ord('Е'): 'E',
                   ord('Ё'): 'E',
                   ord('Ж'): 'Zh',
                   ord('З'): 'Z',
                   ord('И'): 'I',
                   ord('Й'): 'Y',
                   ord('К'): 'K',
                   ord('Л'): 'L',
                   ord('М'): 'M',
                   ord('Н'): 'N',
                   ord('О'): 'O',
                   ord('П'): 'P',
                   ord('Р'): 'R',
                   ord('С'): 'S',
                   ord('Т'): 'T',
                   ord('У'): 'U',
                   ord('Ф'): 'F',
                   ord('Х'): 'H',
                   ord('Ц'): 'Ts',
                   ord('Ч'): 'Ch',
                   ord('Ш'): 'Sh',
                   ord('Щ'): 'Sch',
                   ord('Ъ'): '',
                   ord('Ы'): 'Y',
                   ord('Ь'): '',
                   ord('Э'): 'E',
                   ord('Ю'): 'Yu',
                   ord('Я'): 'Ya',}


    lower_case_letters = {ord('а'): 'a',
                       ord('б'): 'b',
                       ord('в'): 'v',
                       ord('г'): 'g',
                       ord('д'): 'd',
                       ord('е'): 'e',
                       ord('ё'): 'e',
                       ord('ж'): 'zh',
                       ord('з'): 'z',
                       ord('и'): 'i',
                       ord('й'): 'y',
                       ord('к'): 'k',
                       ord('л'): 'l',
                       ord('м'): 'm',
                       ord('н'): 'n',
                       ord('о'): 'o',
                       ord('п'): 'p',
                       ord('р'): 'r',
                       ord('с'): 's',
                       ord('т'): 't',
                       ord('у'): 'u',
                       ord('ф'): 'f',
                       ord('х'): 'h',
                       ord('ц'): 'ts',
                       ord('ч'): 'ch',
                       ord('ш'): 'sh',
                       ord('щ'): 'sch',
                       ord('ъ'): '',
                       ord('ы'): 'y',
                       ord('ь'): '',
                       ord('э'): 'e',
                       ord('ю'): 'yu',
                       ord('я'): 'ya',}

    translit_string = ''


    for index, char in enumerate(sum_string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(sum_string) > index + 1:
                if sum_string[index + 1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char
    #print(translit_string)
    return translit_string

normalize(input_string)        
