# python-notes
Personal notes on using python, mainly python3.  

## Anaconda 

[anaconda distro](https://www.continuum.io/downloads)

## Cookbook snippets

### dedupe a list

```python
a = list(set(a))
```

### invert a list

```python
x_inv = {val : idx for idx, val in enumerate(x)}
```

### char <-> ascii value

```python
>>> ord('a')
97
>>> chr(97)
'a'
```

### read in a file

```python
for line in open("file"):
    print(line)
```
Ok, but does not close file after even after loop exits.

```python
import codecs

for line in codecs.open("file", "r", encoding='ascii', errors='replace'):
    print(line)
```

Read in a CSV file.  
```python
from csv import reader
file = open("filename")
for line in reader(file):
    print(line)
```
Each line is an array of strings.  The big advantage of using csv is that 
it does not view commas in quoted strings as seperators.  

### grab a webpage

```python
import urllib.request

url = "https://google.com"
page = urllib.request.urlopen(url)
html = str(page.read())
```

## matplotlib

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,6]
y = [i*i - 5 * i for i in x]

plt.plot(x,y,"r*-")
plt.xlabel("foo")
plt.ylabel("bar")
plt.title("title")
plt.show()
```
