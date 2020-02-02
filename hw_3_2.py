punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
enter_string = ''
while True:
    text = input('Enter text:')
    enter_string += text.lower()
    if text == '':
        break
str_without_punctuation = enter_string.translate(str.maketrans(punctuation,' '*len(punctuation)))
list_words = str_without_punctuation.split()
print('='*50,'В тексте предоставлены такие слова отсортированные по алфовиту: ','='*50,sep='\n')
for word in sorted(set(list_words)):
    print('{}     {:^10}'.format(word[0].upper(),word))
