import abc


class ABSSearch(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_page(self, word, page_num):
        """
        执行搜索
        :return: 搜索结果页
        """
