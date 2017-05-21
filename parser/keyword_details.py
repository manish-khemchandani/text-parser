class KeywordDetails(object):
    """Class to keep track of all the keywords found on a web page."""

    def __init__(self, keyword):
        self._keyword = keyword
        self._occurrences = 0
        # Number of occurrences of the keyword on the web page.

        self._next_keywords_to_details = {}

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        self._keyword = keyword

    @property
    def next_keywords_to_details(self):
        return self._next_keywords_to_details

    def add_next_keyword(self, keyword):
        next_details = self._next_keywords_to_details.get(keyword, KeywordDetails(keyword))
        next_details.increment_occurrences()
        self._next_keywords_to_details[keyword] = next_details
        return next_details

    def increment_occurrences(self):
        self._occurrences += 1

    def __cmp__(self, other):
        comparison = other._occurrences - self._occurrences
        return comparison if comparison != 0 else cmp(self._keyword, other._keyword)
