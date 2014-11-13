from nltk.corpus import gutenberg

texts = gutenberg.fileids()
with open('gutenberg.txt', 'wb') as f:
    f.write(gutenberg.raw(texts[0]))
