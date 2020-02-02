punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
enter_string = ''
while True:
    text = input('Enter text:')
    enter_string += text.lower()
    if text == '':
        break
str_without_punctuation = enter_string.translate(str.maketrans(punctuation,' '*len(punctuation)))
list_words = str_without_punctuation.split()
print("Статистика слов:")
words_dict = dict()
for word in list_words:
    words_dict[word] = list_words.count(word)
for key,value in words_dict.items():
    print('| {:<15} |  {} |'.format(key,value))
