#--*utf-8*

import collections,re
def get_words(file):
    with open (file) as f:
        words_box=[]
        for line in f:
            words_box.extend(re.split(r'[;\.\s]*', line))
        new_words_box=[]
        for word in words_box:
            if word.isalpha():
                new_words_box.append(word.lower())
    return collections.Counter(new_words_box)
print(get_words('text.txt'))
