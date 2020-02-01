punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
list_word = []
text = input('Enter text:')
list_word = text.split()
while text != '':
    text = input('Enter text:')
    list_word.extend(text.split())
new_string = ' '.join(list_word)
new_text = new_string.translate(str.maketrans(punctuation,' '*len(punctuation)))
l_words = new_text.split()
words_dict = dict()
for word in set(l_words):
    words_dict[word] = l_words.count(word)
print('='*30)
print("Количество слов в веденном тексте показано в таблице ниже:")
print('='*30,end='\n\n')
for key,value in words_dict.items():
    print('| {:<15} |  {} |'.format(key,value))
