
{% comment %}
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(x=0,y=0)
>>> p.x
0
>>> p.y
0
>>> q = Point(x, y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  NameError: name 'x' is not defined
  >>> q = Point(14, 16)
  >>> q
  Point(x=14, y=16)
  >>> q.x
  14
  >>> p
  Point(x=0, y=0)
  >>> x, y = q
  >>> x
  14
  >>> y
  16
  >>>
{% endcomment %}
