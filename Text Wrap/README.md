# Textwrap

The textwrap module provides two convenient functions: wrap() and fill().

[textwrap.wrap()](https://docs.python.org/2/library/textwrap.html#textwrap.wrap)

The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
It returns a list of output lines.

```python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']
```

[textwrap.fill()](https://docs.python.org/2/library/textwrap.html#textwrap.fill)

The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

```python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
```
