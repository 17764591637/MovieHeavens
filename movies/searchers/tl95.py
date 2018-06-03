# -*- coding: utf-8 -*-

from .search_movie_parent import SearchMovieParent

if PY2:
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')


class TL95(SearchMovieParent):
    __slots__ = ['domain']

    def __init__(self):
        self.domain = 'http://www.tl95.com'

    def __get_search_list(self, movie_name):
        url = "%s/?s=".format(self.domain, movie_name)
    

    def get_display_content(self, movie_name):
        return None