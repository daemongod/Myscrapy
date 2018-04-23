# coding:utf8
import urllib.request
class HtmlDownLoader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url.encode('utf-8').decode('utf-8'))
        # if response.read().getcode() != 200:
        #     return None
        return response.read()