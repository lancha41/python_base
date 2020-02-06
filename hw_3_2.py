punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
enter_string = list()
while True:
    text = input('Enter text:')
    enter_string += text.split()
    if text == '':
        break
str_without_punctuation = ' '.join(enter_string).translate(str.maketrans(punctuation,' '*len(punctuation)))
list_words = str_without_punctuation.split()
max_word = 0
print("Статистика слов:")
words_dict = dict()
for word in list_words:
    if len(word) > max_word:
        max_word = len(word)
    words_dict[word] = list_words.count(word)
for word in sorted(list_words):
    print('| {} |'.format(word.ljust(max_word, ' ')))
