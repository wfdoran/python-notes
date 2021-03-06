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

### loop on a dictionary

```python
d = {}
for key in d:
for key, value in d.items():
```

### priority queue

Implement a poor-man's priority queue using =bisect.insort_left= and =pop=.  =insert_left= keeps a list
sorted.  =pop= pulls off the last highest value node.
```python
import bisect
node = (value, state)
queue = []
bisect.insort_left(queue, node)   # insert
node = queue.pop()                # get highest value node
```

### functional list tricks

#### Filter
```python
x = list(range(10))
def f(x):
    return (x%2) == 0
y = [a for a in x if f(a)]
y = filter(f,x)     # note: iterator
y = list(filter(f,x))
y = list(filter(lambda a:(a%2)==0 ,x))
```

#### Map

#### Reduce

#### Add


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

## pandas

[tutorial](https://pandas.pydata.org/pandas-docs/stable/tutorials.html)

## [scipy](scipy.md)

## [parallel](parallel.md)

## nltk

Part of Speach 
```python
import nltk
my_str = "The cow jumped over the moon."
nltk.download()    # first time only
text = nltk.word_tokenize(my_str)
nltk.pos_tag(text)
```
