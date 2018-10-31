"""Case-study #4 Анализ текста
Разработчики:
Селищев А., Паймушкин К., Кривошеенкова Е.

"""

text = input('Введите текст:')
text_lower = text.lower()
num_of_sentences = 0
num_of_words = 1
list_of_vowels = 'аеёиоуыюяэ'
num_of_syllables = 0
for i in text_lower:
    if i == '.':
        num_of_sentences += 1
    if i == ' ':
        num_of_words += 1
    if i in list_of_vowels:
        num_of_syllables += 1
ASL = num_of_words / num_of_sentences
ASW = num_of_syllables / num_of_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
print('Предложений:', num_of_sentences)
print('Слов:', num_of_words)
print('Слогов:', num_of_syllables)
print('Средняя длина предложения в словах:', ASL)
print('Средняя длина слова в слогах:', ASW)
print('Индекс удобочитаемости Флеша:', FRE)
if FRE > 80:
    print('Текст очень легко читается (для младших школьников).')
elif 50 < FRE <= 80:
    print('Простой текст (для школьников).')
elif 25 < FRE <= 50:
    print('Текст немного трудно читать (для студентов).')
elif FRE <= 25:
    print('Текст трудно читается (для выпускников ВУЗов).')
