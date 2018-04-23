# coding:utf8
import re
import urllib.parse
from bs4 import BeautifulSoup
class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return  new_urls,new_data
    # <a target="_blank" href="/item/%E6%BA%90%E4%BB%A3%E7%A0%81/3969" data-lemmaid="3969">源代码</a>
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        url_nodes = soup.find_all('a',href=re.compile(r"/item/*"))
        new_full_url = ''
        for url_node in url_nodes:
            if url_node.has_attr('data-lemmaid'):
                new_full_url = r"https://baike.baidu.com"+ url_node['href'] +r"/"+url_node['data-lemmaid']
                new_urls.add(new_full_url)
            else:
                new_full_url = r"https://baike.baidu.com"+ url_node['href']
                new_urls.add(new_full_url)

        return new_urls
    def _get_new_data(self,page_url,soup):
        title_content = {}
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        title = title_node.get_text()
        content_nodes = soup.find_all('div',class_ = 'para')
        content = []
        for content_node in content_nodes:
            content.append(content_node.get_text())
        content_string = ''.join(content)
        title_content['title'] = title
        title_content['content'] = content_string
        # return  title_content
        return content_string