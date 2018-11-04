"""Case-study #4 Анализ текста
Разработчики:
Селищев А., Паймушкин К., Кривошеенкова Е.

"""
import ru_local
text = input('{}'.format(ru_local.TEXT))
text_lower = text.lower()
num_of_sentences = 0
num_of_words = 1
list_of_vowels = '{}'.format(ru_local.AE)
num_of_syllables = 0
for i in text_lower:
    if i == '.' or i == '!' or i == '?':
        num_of_sentences += 1
    if i == ' ':
        num_of_words += 1
    if i in list_of_vowels:
        num_of_syllables += 1
ASL = num_of_words / num_of_sentences
ASW = num_of_syllables / num_of_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
print('{}'.format(ru_local.SUP), num_of_sentences)
print('{}'.format(ru_local.WORD), num_of_words)
print('{}'.format(ru_local.SYL), num_of_syllables)
print('{}'.format(ru_local.SENT), ASL)
print('{}'.format(ru_local.MDW), ASW)
print('{}'.format(ru_local.IND), FRE)
if FRE > 80:
    print('{}'.format(ru_local.EASY))
elif 50 < FRE <= 80:
    print('{}'.format(ru_local.SCHOOL))
elif 25 < FRE <= 50:
    print('{}'.format(ru_local.STUD))
elif FRE <= 25:
    print('{}'.format(ru_local.HARD))