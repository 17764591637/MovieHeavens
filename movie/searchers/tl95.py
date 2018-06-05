# -*- coding: utf-8 -*-

from .search_movie_parent import SearchMovieParent
from .._compat import PY2
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
import requests
import re

if PY2:
    import sys
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')


class TL95(SearchMovieParent):
    __slots__ = ['domain', 'pool']

    def __init__(self):
        self.domain = 'http://www.tl95.com'
        self.pool = ThreadPool(8)

    def __get_search_list(self, movie_name):
        url = "{0}/?s={1}".format(self.domain, movie_name)
        res = requests.get(url, headers = super(TL95, self).get_headers(), timeout= 10)
        soup = BeautifulSoup(res.content,"html.parser")
        a_list = soup.find_all('a',rel='bookmark')
        a_href_list = [a['href'] for a in a_list]
        return [a['href'] for a in a_list]

    def __parse_content(self,url):

        down_url_list = []

        res = requests.get(url,headers = super(TL95, self).get_headers(), timeout= 10)
        
        soup = BeautifulSoup(res.content, "html.parser")
        # 电驴的链接
        a_dl = soup.find_all(href=re.compile('ed2k'))

        # 百度网盘链接
        a_bd = soup.find_all(href=re.compile('https://pan.baidu.com'))
       
        # 磁力链接
        a_magnet = soup.find_all(href=re.compile('magnet:'))
        
        # 迅雷
        a_thunder_list = soup.find_all(href=re.compile('thunder://'))

        if any(a_dl):
            down_url_list.append(a_dl[0]['href'])
        if any(a_bd):
            p = a_bd[0].find_parent('p')
            down_url_list.append(p.text)
        if any(a_magnet):
            down_url_list.append(a_magnet[0]['href'])
        if any(a_thunder_list):
            for a in a_thunder_list:
                down_url_list.append(a['href'])
        return down_url_list
        

    def get_display_content(self, movie_name):
        tmp_down_url_list = self.pool.map(self.__parse_content, self.__get_search_list(movie_name))
        down_url_list = []
        for url_list in tmp_down_url_list:
            if any(url_list):
                for down_url in url_list:
                    down_url_list.append(down_url)
        return down_url_list