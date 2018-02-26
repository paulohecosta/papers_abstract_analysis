import nltk
from nltk.corpus import stopwords


def tokenize_abstract(abstract):
    """
    Tokenize an abstract and set all tokens to lower
    :param abstract: string with full article abstract
    :return: list of tokens
    """
    tokens = nltk.word_tokenize(abstract)
    new_tokens = []
    for token in tokens:
        new_tokens.append(token.lower())
    return new_tokens


def cleanup_tokens(tokens):
    """
    Clean abstract and common tokens from token list
    :param tokens: list of tokens
    :return: list of important tokens
    """
    stopset = set(stopwords.words('english'))
    cleanup = [i for i in tokens if i not in stopset if len(i) > 2]
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
