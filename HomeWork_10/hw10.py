# Даны два списка чисел. Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания.

# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

#print(*sorted(set(input().split()) & set(input().split()), key=int))



#Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), 
#если это число ранее встречалось в последовательности или NO, если не встречалось.
#Пример:
#Входные данные: 1 2 3 2 3 4
#Выходные данные:
#NO
#NO
#NO
#YES
#YES
#NO

'''used = set()
for i in raw_input().split():
    n = int(i)
    if n in used:
        print('YES')
    else:
        print('NO')
        used.add(n)
        '''
        
        
        
'''Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность не пробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

Sample Input:

4
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

Sample Output:

19  '''

n = int(input())
# чтобы не вводить текст, читаем его из файла
with open('file.txt', 'r') as fh:
    text = fh.readlines()[:n] # выбираем нужное число строк
    
    
# импортируем нужные модули
import re
from string import punctuation

# паттерн для удаления знаков препинания
regex = re.compile('[%s]' % re.escape(punctuation))

# удаляем пунктуацию и преобразуем слова к нижнему регистру
text = [re.sub('\s+', ' ', regex.sub(' ', i)).strip().lower().split() for i in text]

# выводим количество уникальных слов
print(len({j for i in text for j in i}))


