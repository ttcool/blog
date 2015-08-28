# CSV文件读取
```python
#!/usr/bin/env python

import csv

filename = 'ch02-data.csv'

data = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        c = 0
        for row in reader:
            if c == 0:
                header = row
            else:
                data.append(row)
            c += 1
except csv.Error as e:
    print "Error reading CSV file at line %s: %s" % (reader.line_num, e)
    sys.exit(-1)

if header:
    print header
    print '=================='

for datarow in data:
    print datarow
```

csv文件内容如下

"day","ammount"
2013-01-24,323
2013-01-25,233
2013-01-26,433
2013-01-27,555
2013-01-28,123
2013-01-29,0
2013-01-30,221
