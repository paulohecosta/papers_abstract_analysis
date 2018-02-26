from custom_entities.author import AuthorData
from custom_entities.journal import JournalData
from custom_helpers.nltk_helper import get_important_words


class ArticleData(object):
    def __init__(self, root):
        self.article_title = root.find(".//ArticleTitle").text
        self.pub_date = root.find(".//PubDate/Day").text + "/" + \
                        root.find(".//PubDate/Month").text + "/" + \
                        root.find(".//PubDate/Year").text
        self.doi = root.find(".//*[@IdType='doi']").text

        self.abstract_text = ""
        for texts in root.findall(".//AbstractText"):
            self.abstract_text += "\n" + texts.text

        self.key_words = []
        concat_words = ""
        for key_word in root.findall(".//Keyword"):
            concat_words += " " + key_word.text
        for token in get_important_words(concat_words, 5):
            self.key_words.append(str(token[0]))

        self.journal = JournalData(root.find(".//Journal/ISSN").text, root.find(".//Journal/Title").text)

        self.authors = []
        for author in root.findall(".//Author"):
            self.authors.append(AuthorData(author.find("LastName"), author.find("ForeName")))

        self.important_words = []
        for token in get_important_words(self.abstract_text, 10):
            self.important_words.append(str(token[0]))

        self.ordered_keys = list(set( list(set(self.key_words)) + list(set(self.important_words)) ))