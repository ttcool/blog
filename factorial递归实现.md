#factorial递归实现

```python
def factorial(n):
    if n == 0:
        result = 1
        print "%f" % result
        return result
    else:
        recurse  = factorial(n-1)
        result = n*recurse
        print "%f" % result
        return result


factorial(8)

```

