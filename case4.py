"""Case-study #4 Анализ текста
Разработчики:
Селищев А., Паймушкин К., Кривошеенкова Е.

"""
import ru_local
text = input('{}'.format(ru_local.TEXT))
text_lower = text.lower()
count_sentens = 0
count_words = 1
list_of_vowels = '{}'.format(ru_local.AE)
count_syllables = 0
for i in text_lower:
    if i == '.' or i == '!' or i == '?':
        count_sentens += 1
    if i == ' ':
        count_words += 1
    if i in list_of_vowels:
        count_syllables += 1
ASL = count_words / count_sentens
ASW = count_syllables / count_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
print('{}'.format(ru_local.SUP), count_sentens)
print('{}'.format(ru_local.WORD), count_words)
print('{}'.format(ru_local.SYL), count_syllables)
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
