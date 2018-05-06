from flask import url_for

class Page:
    """
    The Page Objects to be used to define attributes of the 
    rendered pages.
    """

    title = ""
    lang = "en"
    keywords = []

    def __init__(self, title, *args):
        self.title = title
        self.maincss =  url_for('static', filename = "css/main.css")
        
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

    
    
class Tsumo:
    """
    The Tsumo Object
    """
    
    
    def __init__(self, id = None , tsumo = None, translation = None, explanation = None):
        
        if id is not None:
            self.id = id
        else:
            self.id = 1

        if tsumo is not None:
            self.tsumo = tsumo

        else: 
            tsumo = ""

        if translation is not None:
            self.translation = translation
        else:
            self.translation = ""
        
        if explanation is not None:
            self.explanation = ""

        
