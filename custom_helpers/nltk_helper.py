import codecs
import nltk
from nltk.corpus import stopwords


def tokenfy_abstract(abstract):
    tokens = nltk.word_tokenize(abstract)
    new_tokens = []
    for token in tokens:
        new_tokens.append(token.lower())
    return new_tokens


def cleanup_text(tokens):
    stopset = set(stopwords.words('english'))
    cleanup = [i for i in tokens if i not in stopset if len(i) > 2]
    return cleanup


def get_important_words(abstract, quantity):
    tokens = tokenfy_abstract(abstract)
    clean_tokens = cleanup_text(tokens)
    fdist = nltk.FreqDist(clean_tokens)
    return fdist.most_common(quantity)
