import nltk
from nltk.corpus import stopwords
import re


def has_numbers(input):
    return bool(re.search(r'\d', input))


def tokenize_abstract(abstract):
    """
    Tokenize an abstract and set all tokens to lower
    :param abstract: string with full article abstract
    :return: list of tokens
    """
    tokens = nltk.word_tokenize(abstract)
    tagged = nltk.pos_tag(tokens)
    new_tokens = []
    # remove verbs
    for tag in tagged:
        if str(tag[1]) == 'VBG' or str(tag[1]) == 'VBN' or str(tag[1]) == 'VBD' or str(tag[1]) == 'VBZ':
            break
        new_tokens.append(tag[0])
    new_tokens_2 = []
    # lower words
    for token in new_tokens:
        new_tokens_2.append(token.lower())
    #stem words
    stemmer = nltk.PorterStemmer()
    new_tokens_3 = []
    for token in new_tokens_2:
        new_tokens_3.append(stemmer.stem(token))
    return new_tokens_3


def cleanup_tokens(tokens):
    """
    Clean abstract and common tokens from token list
    :param tokens: list of tokens
    :return: list of important tokens
    """
    stopset = set(stopwords.words('english'))
    cleanup = [i for i in tokens if i not in stopset if len(i) > 4 if has_numbers(i) is False]
    return cleanup


def get_important_words(abstract, quantity):
    """
    This method recovers a list of important tokens with the given quantity
    :param abstract: string with full article abstract
    :param quantity: quantity of returned tokens
    :return: list of tokens
    """
    tokens = tokenize_abstract(abstract)
    clean_tokens = cleanup_tokens(tokens)
    fdist = nltk.FreqDist(clean_tokens)
    return fdist.most_common(quantity)
