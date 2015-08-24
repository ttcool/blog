# 安装
$ apt-get install python-bs4

$ easy_install beautifulsoup4
 
$ pip install beautifulsoup4

```python

import urllib2
from bs4 import BeautifulSoup
import json


headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
url = 'http://liansai.500.com/index.php?c=score&a=getmatch&stid=7471&round=1'
req = urllib2.Request(url,headers=headers)
content = urllib2.urlopen(req).read()
con = BeautifulSoup(content,from_encoding='GB18030')
c = json.loads(content)
for i in c:
    for k,v in i.items():
        print k,v
        

```


