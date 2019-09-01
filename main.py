
from searches import *
from collector import Collector


if __name__ == '__main__':

    # 单输入的处理
    arg_word = 'qq.com'
    arg_engine = 'baidu'

    search_factor = {
        'bing': BingSearch,
        'baidu': BaiDuSearch,
        'google': GoogleSearch
    }

    engine = search_factor.get(arg_engine)

    collector = Collector(engine, arg_word)
    collector.process()
    domains = collector.get_domains()
    emails = collector.get_emails()

    print(domains)
    print(emails)

