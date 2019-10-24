from nltk.corpus import wordnet
print(wordnet.synset('advantage.n.01').path_similarity(wordnet.synset('advantage.n.01')))