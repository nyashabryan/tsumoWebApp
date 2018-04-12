from flask import url_for

class Page:
    """ The Page Objects to be used to define attributes of the 
        rendered pages.
    """

    title = ""
    maincss = ""
    lang = "en"
    keywords = []

    def __init__(self, title):
        self.title = title
        
    def change_lang(self, lang):
        self.lang = lang

    def add_keywords(self, keywords):
        if (isinstance(keywords, "String".__class__)):
            self.keywords.append(keywords)
            return True

        elif (isinstance(keywords, [].__class__)):
            self.keywords = self.keywords + keywords
            return True

        else:
            return False
    
    def add_css(self, css):
        self.maincss =  css


