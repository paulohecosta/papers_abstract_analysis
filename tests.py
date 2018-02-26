# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import sklearn
import requests
import base64
import seaborn as sns
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('stopwords')
import os
import glob
import xml.etree.ElementTree

from custom_entities.article import ArticleData
from custom_helpers.nltk_helper import get_important_words

path = 'C:\Users\Paulo\Documents\PyCharmProjects\papers_abstract_analysis\papers'

for filename in glob.glob(os.path.join(path, '*.xml')):
    root = xml.etree.ElementTree.parse(filename).getroot()
    article = ArticleData(root)

    print("")
    print(article.article_title)
    print(get_important_words(article.abstract_text, 10))
