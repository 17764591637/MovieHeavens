# -*- coding: utf-8 -*-
from movie.searchers.movie_heaven import MovieHeaven
from movie.searchers.tl95 import TL95

if __name__ == '__main__':
    a = TL95()
    print(a.get_display_content("我爱你"))