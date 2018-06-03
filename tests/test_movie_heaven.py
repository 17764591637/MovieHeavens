# -*- coding:utf-8 -*-

from movie.searchers.movie_heaven import MovieHeaven
import pytest


@pytest.mark.parametrize("url,params,excepted", [
    ("http://s.dydytt.net/plus/search.php", {"kwtype": "0", "searchtype": "title", "keyword": "功夫"}, True),
    ("http://s.dydytt.net/plus/search.php", {"kwtype": "0", "searchtype": "title", "keyword": ""}, False)
])
def test_get_display_content(url, params, excepted):
    a = MovieHeaven()
    url = url
    params = params
    res_list = a.get_display_content(url, params)
    flag = len(res_list) > 0 and res_list != ['Not Found']
    assert flag == excepted
