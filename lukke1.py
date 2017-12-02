

def make_dict(s):
    dict_s = {}
    for el in s:
        if el in dict_s:
            dict_s[el] += 1
        else:
            dict_s[el] = 1
    return dict_s

def five_gram(s):
    new_string = ''
    for i in range(len(s) - 4):
        new_string += s[i:(i + 5)]
    return new_string


original_word = 'aeteesasrsssstaesersrrsse'
set_s = set(original_word)
dict_original = make_dict(original_word)
words_to_test = []
length = 9

with open('wordlist.txt', 'r') as wordlist:
    w_list = wordlist.read().split('\n')
    for word in w_list:
        if len(word) == length and set_s == set(word):
            words_to_test.append(word)


for word in words_to_test:
    test_word = five_gram(word)
    test_dict = make_dict(test_word)
    for el in set_s:
        correct = True
        if el in dict_original and el in test_dict and dict_original[el] != test_dict[el]:
            correct = False
    if correct:
        print('this matches: ', word)