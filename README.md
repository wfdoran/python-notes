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
