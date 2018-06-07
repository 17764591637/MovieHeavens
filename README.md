# MovieHeavens

基于Tkinter的电影搜索工具

### 关于开发
最初为了避免找电影期间的各种广告,以及各种页面跳转
Tk版本相较于Qt版本新增了搜索片源

### 使用

命令行下

```python
python3 startup.py
```

### 打包

确保安装 pyinstaller

```python
pyinstaller -w -F startup.py -p movie\__init__.py -p movie\_compat.py -p movie\searchers\__init__.py -p movie\searchers\movie_heaven.py -p movie\searchers\search_movie_parent.py -p movie\searchers\tl95.py -i movie.ico
```

### 可执行程序

[Linux版本](https://pan.baidu.com/s/1Pd3NrJRmsPeZmJrIbCxJAA)

[Windows版本](https://pan.baidu.com/s/1xVwUSlA4mAp-YQjPSUirlw)

[Tk-Windows版本](https://pan.baidu.com/s/1tYK7ca1GWONaLKKSekfYPw)

### 其他版本

[Electron版本](https://github.com/lt94/electron-searchMovies)

### 捐赠

如果我的项目对您有帮助，欢迎捐赠

<table>
  <tr>
    <th width="50%">支付宝</th>
    <th width="50%">微信</th>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><img width="70%" src="http://ww1.sinaimg.cn/large/006wYWbGly1fm10itkjb6j30aj0a9t8w.jpg"></td>
    <td><img width="70%" src="http://ww1.sinaimg.cn/large/006wYWbGly1fm10jihygsj309r09tglw.jpg"></td>
  </tr>
</table>
