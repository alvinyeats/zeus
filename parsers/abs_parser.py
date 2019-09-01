import abc


class ABSParser(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_domain(self, html):
        """
        从html中提取域名信息
        :param html:
        :return: 搜索结果页
        """

    @abc.abstractmethod
    def get_email(self, html):
        """
        从html中提取邮箱信息
        :param html:
        :return:
        """
