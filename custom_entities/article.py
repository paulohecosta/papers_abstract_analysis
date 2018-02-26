from custom_entities.author import AuthorData
from custom_entities.journal import JournalData


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
        for key_word in root.findall(".//Keyword"):
            self.key_words.append(key_word.text)

        self.journal = JournalData(root.find(".//Journal/ISSN").text, root.find(".//Journal/Title").text)

        self.authors = []
        for author in root.findall(".//Author"):
            self.authors.append(AuthorData(author.find("LastName"), author.find("ForeName")))
