result = {}
for filename in range(1, 7):
    with open(f'{filename}', 'r', encoding='utf-8') as input_file:
        input_data = input_file.read()
    with open(f'{filename}.clue', 'r', encoding='utf-8') as clue_file:
        output_data = clue_file.read()
    result[input_data] = output_data
print(result[input_data])
with open(f'result_dic.txt', 'w', encoding='utf-8') as result_dic:
    result_dic.write(str(result))
# print(result)