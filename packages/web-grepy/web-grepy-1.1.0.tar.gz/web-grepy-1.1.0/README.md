# web-grepy: CommandLine web-grep.py

![](https://img.shields.io/static/v1?label=+&message=Python%203.9%2B&color=lightblue&logo=Python&style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/web-grepy.svg?style=flat-square)](https://pypi.python.org/pypi/web-grepy)

Re-implementation [web-grep](https://github.com/cympfh/web-grep) with Python3,  
Scraping HTML or XML with simple Pattern Matching like `grep -o`.

```bash
# Requires Python3
$ pip install web-grepy
$ which web-grepy
$ curl -sL https://example.com/xxx | web-grepy '<a href={}></a>'
$ curl -sL https://example.com/xxx | web-grepy '<a href={link}>{text}</a>'  # ltsv by default
$ curl -sL https://example.com/xxx | web-grepy '<a href={link}>{text}</a>' -f json
```
