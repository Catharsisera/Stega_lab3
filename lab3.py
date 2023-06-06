import re

fileText = open("lab3_input.txt", 'r', encoding='utf-8')

ArrLenString = []
# for i in fileText:
#     ArrLenString.append(len(i))
# print('len paragraphs:', ArrLenString)

symbols = r"[^А-я \n]"
arrY = []
arrN = []
textY = ''
textN = ''
outText = ''

for n, line in enumerate(fileText):
    if re.findall(symbols, line):
        textY += line
        outText += 'YES - {}'.format(line)
        arrY.append(n + 1)
    else:
        textN += line
        outText += ('NO - {}'.format(line))
        arrN.append(n + 1)

print('-----Метод пунктуация-----')
print('Строки множества Y:', arrY)
print('Строки множества N:', arrN, '\n')

print('-----Текст-----\n', outText)

print("\n-----Строки со скрытой информацией-----")
print(textY, '\n')
print("\n-----Строки без скрытой информацией-----")
print(textN)