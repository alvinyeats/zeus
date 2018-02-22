# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import sys
from datetime import datetime

from bs4 import BeautifulSoup
from django.db.utils import IntegrityError

from apps.spider.models import NVD
from apps.spider.tools.common import CVE_KEY_WORDS1
from apps.spider.tools.crawler_error_mail import crawler_error
from utils.crawler import CrawlerImp


class CrawlerNVD(CrawlerImp):

    def today_nvd_parse(self):
        html = self.get_page()
        if not html:
            crawler_error(str(self.url))
            return
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', id='latestVulns')
        if not ul:
            return

        lis = ul.find_all('li')
        for li in lis:
            sub_url = li.find('a')['href']
            origin_url = self.url_merge(sub_url[1:])

            nvd_html = self.get_sub_page()
            if not nvd_html:
                continue
            nvd_soup = BeautifulSoup(nvd_html, 'lxml')

            cve_info = nvd_soup.find('dl', class_='dl-horizontal')
            cve_dds = cve_info.find_all('dd')
            if len(cve_dds) < 3:
                continue
            title = cve_dds[0].get_text().strip()
            release_time = datetime.strptime(cve_dds[1].get_text().strip(), "%m/%d/%Y").strftime("%Y-%m-%d")
            revise_time = datetime.strptime(cve_dds[2].get_text().strip(), "%m/%d/%Y").strftime("%Y-%m-%d")

            content = nvd_soup.find('p', {'data-testid': 'vuln-description'}).get_text().strip()
            solution_url = nvd_soup.find('td', {'data-testid': 'vuln-hyperlinks-link-0'}).find('a')['href']

            influence = ""
            influence_div = nvd_soup.find('div', id='p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_'
                                                    'zoneCenter_VulnerabilityDetail_VulnFormView_VulnConfigurationsDiv')

            influence_spans = influence_div.find_all('span')

            if len(influence_spans) < 3:
                continue
            for influence_span in influence_spans[2:]:
                influence += influence_span.get_text().strip() + '\r\n'

            # print release_time
            # print revise_time
            self._save_nvd_data(origin_url, title, release_time, revise_time, content, solution_url, influence)

    @staticmethod
    def _save_nvd_data(origin_url, title, release_time, revise_time, content, solution_url, influence):
        pat = re.compile('|'.join(CVE_KEY_WORDS1), flags=re.IGNORECASE)
        key_word = ';'.join(set(pat.findall(content)))

        if NVD.objects.filter(title=title):
            sys.stdout.write(str(title) + " already exist, start updating\n")
            # 禁止更新，如果人工登记漏洞后，nvd官方又进行了发布，那么将会重复报告漏洞，
            # 且官方英文不如管理员手动登记的可读性高
            # cve_obj = NVD.objects.get(title=title)
            # cve_obj.key_word = key_word
            # cve_obj.revise_time = revise_time
            # cve_obj.influence = influence
            # cve_obj.content = content
            # cve_obj.save()
            # sys.stdout.write("Update success\n")
        else:
            sys.stdout.write(str(title) + ", start create new data\n")
            try:
                cve_obj = NVD(
                    title=title,
                    key_word=key_word,
                    release_time=release_time,
                    revise_time=revise_time,
                    influence=influence,
                    content=content,
                    origin_url=origin_url,
                    solution_url=solution_url,
                )
                cve_obj.save()
                sys.stdout.write("Save success\n")
            except IntegrityError, e:
                sys.stdout.write(str(e))

    def start(self):
        self.today_nvd_parse()
