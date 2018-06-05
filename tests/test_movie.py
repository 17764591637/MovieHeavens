# -*- coding:utf-8 -*-

from movie import get_all_down_url_list
import pytest


@pytest.mark.parametrize("movie_name,excepted", [
    ("我爱你", True)
])
def test_get_all_down_url_list(movie_name, excepted):
    res_list = get_all_down_url_list(movie_name)
    flag = len(res_list) > 0 and res_list != ['Not Found']
    assert flag == excepted
