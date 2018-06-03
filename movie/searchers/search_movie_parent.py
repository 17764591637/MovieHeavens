# -*- coding:utf-8 -*-
from fake_useragent import UserAgent

class SearchMovieParent:
    """
        the parant of all searchmovies class
    """

    def get_headers(self):
        return {"User-Agent": UserAgent().random}

    def get_display_content(self, url, params=None):
        return None
