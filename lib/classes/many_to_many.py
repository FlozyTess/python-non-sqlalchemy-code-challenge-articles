class Article:
    all = [] # we use this to store all the articles
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # to store each article in a list
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value

    @classmethod
    def clear_all(cls):
        """Helper method to reset all articles before testing"""
        cls.all = []
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise ValueError("Name must be a non-empty string")
        self.name = name

    def articles(self):
        """Returns a list of articles written by this author"""
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass