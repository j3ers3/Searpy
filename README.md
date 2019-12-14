# 🥀 Searpy ![Stage](https://img.shields.io/badge/Release-STABLE-brightgreen.svg) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-2.0-red.svg)

🔧 批量搜索工具，用于渗透中采集。

![](./pic/banner.png){:height="400" width="700"}

## 搜索引擎
- [x] Shodan
- [x] Fofa
- [ ] Zoomeye
- [x] Google
- [x] Baidu
- [x] Bing
- [x] 360so
- [x] goo

## Install
```
git clone https://github.com/j3ers3/Searpy
pip install -r requirement.txt

配置API账号 ./util/config.py

python Searpy -h
```


## Help
```bash
python Searpy.py --fofa -s "app:jboss" -p 1

python Searpy.py --shodan -s "weblogic" -l 10 

python Searpy.py --google -s "inurl:login.action" -p 1

```


![](./pic/fofa.png){:height="550" width="700"}

![](./pic/google.png){:height="500" width="700"}



## 其他功能
利用Shodan网站图标hash来寻找使用相同图标的网站，可用于溯源真实IP和资产发现

`python Searpy.py --shodan_ico https://www.qq.com`

![](./pic/ico.png){:height="450" width="700"}


## 模块调用
```python
>>> from Searpy import Bing
>>> s = Bing('inurl:php?id=1', 2)
>>> s.search()
>>> for i in s.result:
>>>     print(i)
```


## Donations
* XMR: `498AoZRwfC11Fa4LwAyVVp3wRD4Zyf1e1HziegczeWeSYVVTZ8gw8CoNPm5yhY91tkDqDMBg6A5KUfyowMtdkQDrDxE5aVN`
* BTC: `1ALWC7rGL4dHgbyy4R8uTVHmDugPDD7Rvt`

## Contact
- [Twitter](https://twitter.com/j3ers3)
