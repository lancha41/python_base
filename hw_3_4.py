def get_vocabluary(text):
    result = {}
    punctuation = '..'
    str_without_punctuation = text.translate(str.maketrans(punctuation, ' ' * len(punctuation)))
    list_words = sorted(str_without_punctuation.split())
    not_trans_words = set(list_words)
    for word in set(list_words):
        while True:
            count_errors = 0
            trans = input('Введите перевод слова "{}" на английский язык:'.format(word))
            for ch in punctuation:
                if ch in trans:
                    count_errors += 1
            if trans == '':
                count_errors += 1
            if count_errors != 0:
                print('Ошибка! Введите еще раз перевод.')
            else:
                break
        result[word] = trans
    return result
if __name__ == "__main__":
    TEXT = """Пользователь может .."""
    vocabluary = get_vocabluary(TEXT)
    print("Словарь переводов указан в таблице ниже:")
    max_word = 0
    max_trans = 0
    for word,word_tr in vocabluary.items():
        if len(word) > max_word:
            max_word = len(word)
        if len(word_tr) > max_trans:
            max_trans = len(word_tr)
    for key,value in vocabluary.items():
        print('| {} |  {} |'.format(key.center(max_word,' '), value.center(max_trans,' ')))
