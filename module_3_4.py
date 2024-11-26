
def single_root_words(root_word , *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() == word.lower():
            same_words.append(word)
        elif root_word.lower() in word.lower():
            same_words.append(word)

    return same_words

result1 = single_root_words('гриб', 'грибник', 'грибок', 'грибной', 'грибница')
result2 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result3 = single_root_words('Able', 'disablement', 'Disabling ', 'Disable', 'Bagel')

print(result1)
print(result2)
print(result3)