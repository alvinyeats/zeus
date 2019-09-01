
from searchs import *
from parsers import *
from collector import Collector


if __name__ == '__main__':

    # 单输入的处理
    arg_word = 'qq.com'
    arg_engine = 'google'

    parser_factor = {
        'regex': RegexParser,
        'str': StrParser
    }

    search_factor = {
        'baidu': BaiDuSearch,
        'google': GoogleSearch
    }

    parser = RegexParser
    engine = search_factor.get(arg_engine)

    collector = Collector(engine, parser)
    html = collector.search(arg_word)
    domains = collector.get_domain(html)
    emails = collector.get_email(html)

