class Article:
    all = [] # we use this to store all the articles
    def __init__(self, author, magazine, title):
        self._author = author
        self.magazine = magazine
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("title must be a non-empty string")
        self._title = title
        Article.all.append(self)  # to store each article in a list
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        """Prevent modifying the title after initialization."""
        raise AttributeError("title is an immutable string") 
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
        self._name = name  # Author's name should be immutable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Author name is immutable")
    def articles(self):
        """Returns a list of articles written by this author"""
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        """Returns a unique list of magazines the author has written for"""
        return list(set(article.magazine for article in self.articles()))
        pass

    def add_article(self, magazine, title):
        """Allows an author to write an article for a magazine"""
        return Article(self, magazine, title)
        pass

    def topic_areas(self):
        """Returns a unique list of magazine categories the author has written for"""
        categories = {article.magazine.category for article in self.articles() if article.magazine and article.magazine.category}
        return list(categories) if categories else None
        pass

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string with 2 to 16 characters")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self.category = category
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be a string with 2 to 16 characters")
        self._name = value  #to allow name updating

    def articles(self):
        """Returns a list of articles published in this magazine"""
        return [article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        """Returns a list of unique authors who have contributed to this magazine"""
        return list(set(article.author for article in self.articles()))
        pass

    def article_titles(self):
        """Returns a list of article titles published in this magazine"""
        return [article.title for article in self.articles()]
        pass

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles for this magazine"""
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1

        return [author for author, count in author_count.items() if count > 2]
        pass