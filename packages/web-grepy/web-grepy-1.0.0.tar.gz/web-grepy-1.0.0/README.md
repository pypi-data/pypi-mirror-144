# web-grepy: CommandLine web-grep.py

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
