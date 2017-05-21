class KeywordDict(object):
    """Class to keep track of all the keywords found on a web page.

    This class uses a dict to keep track of all the single- as well as multi-word phrases found in
    a web page.
    """

    def __init__(self):
        self._keyword_to_details = {}

    def get(self, keyword):
        """Get the Keyword Details from the dict for a keyword.

        :param keyword: The keyword for which the Keyword Details are to be fetched.
        :return: KeywordDetails
        """
        return self._keyword_to_details.get(keyword)

    def add(self, keywords):
        """Add a multi-word phrase to the dict.

        :param keywords:
        :return:
        """
        pass
