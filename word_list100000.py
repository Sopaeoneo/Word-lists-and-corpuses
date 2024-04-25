import nltk
import pymorphy3
import re

nltk.download('punkt')
filename = (r"\частотные словари\corpuses\100000.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()

morph = pymorphy3.MorphAnalyzer()

lemmas = []
for line in lines:
    tokens = nltk.word_tokenize(line)
    for token in tokens:
        token = morph.parse(token)[0].normal_form
        lemmas.append(token)

only_words = []
for word in lemmas:
    word = word.lower()
    if word[0] in ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]:
        word = re.sub(r'(\w+)(.—)', r'\1', word)
        word = re.sub(r'(\w+)(.\')', r'\1', word)
        only_words.append(word)

not_repeating = []
for word in only_words:
    if word in not_repeating:
        continue
    else:
        not_repeating.append(word)

list_of_words = []
for word in not_repeating:
    count = only_words.count(word)
    ipm = only_words.count(word)/len(only_words) * 1000000
    list_of_words.append([word, count, ipm])

list_of_words.sort(key=lambda x: x[1], reverse=True)
f = open(r'\частотные словари\word_lists\word_list100000.txt', 'w', encoding="utf-8")
f.write(str(list_of_words))
f.close
print(list_of_words[0:30])
