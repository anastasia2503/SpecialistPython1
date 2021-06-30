# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

# TODO: your code here
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
text = text.replace('.', '')
text = text.replace(',', '')
parts = text.split(' ')
print(parts)
x = 0
res = 0
while x < len(parts):
    if len(parts[x]) > 7:
        res += 1
    else:
        pass
    x += 1
print(res)
