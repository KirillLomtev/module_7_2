def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_position = {}
    for i in range(len(strings)):
        supp_tuple = (i+1, file.tell())

        string_position[supp_tuple] = strings[i]

        file.write(f'{strings[i]}\n')


    file.close()
    return string_position
info = [
    'Text for tell.',
     'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)