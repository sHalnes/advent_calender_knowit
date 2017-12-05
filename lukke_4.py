'''Ordet “regninger” er et palindrom, det leses likt fremlengs og baklengs. Ordet “tartar” er ikke et palindrom, men
anagrammet “rattar” er det. Hvor mange ord fra denne ordlisten er ikke et palindrom, men har ett eller flere anagram som er det?'''


def anagram(word):
    odd = False
    word_stat = {}
    for ch in word:
        if ch not in word_stat:
            word_stat[ch] = 1
        else:
            word_stat[ch] += 1
    for key in word_stat:
        if word_stat[key]%2 == 1 and odd:
            return False
        elif word_stat[key] % 2 == 1 and not odd:
            odd = True
    return True

file_name = 'anagramlist.txt'
anagrams = []
with open(file_name, 'r') as file:
    data = file.read().split('\n')
    # check if a word is a palindrone
    for word in data:
        for i in range(len(word)//2):
            if word[i] != word[-(i+1)]:
                is_anagram = anagram(word)
                if is_anagram:
                    anagrams.append(word)
                break
print(len(anagrams))
