import abc


class ABSSearch(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process(self):
        """
        执行搜索
        :return: 搜索结果页
        """
