
class Collector:

    def __init__(self, engine, parser):
        """
        :param engine: searchs engine class
        """
        self.engine = engine()
        self.parser = parser()

    def search(self, word):
        return self.engine.search(word)

    def get_domain(self, word):
        return self.parser.get_domain(word)

    def get_email(self, html):
        return self.parser.get_email(html)

    def to_string(self):
        pass

    def write(self):
        pass

