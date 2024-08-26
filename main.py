def custom_write(file_name, strings):
    strings_positions = {}
    num_str = 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            num_bite = file.tell()
            file.write(i + "\n")
            strings_positions[(num_str, num_bite)] = i
            num_str += 1
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
print(result)