import re
import time


class Collector:

    def __init__(self, engine, word):
        self.page_limit = 100
        self.engine = engine()
        self.word = word
        self.domains = []
        self.emails = []

    def _extract_domains(self, html):
        reg_hosts = re.compile('[a-zA-Z0-9.-]*\.' + self.word)
        temp = reg_hosts.findall(html)
        return list(set(temp))

    def process(self):
        counter = 0
        while counter <= self.page_limit:
            html = self.engine.get_page(self.word, counter)
            self.domains += self._extract_domains(html)
            time.sleep(1)

            print("\tSearching " + str(counter) + " results...")
            counter += 10

    def get_domains(self):
        return self.domains

    def get_emails(self):
        return self.emails

    def to_string(self):
        pass

    def write(self):
        pass

