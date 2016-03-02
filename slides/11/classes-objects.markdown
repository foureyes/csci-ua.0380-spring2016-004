---
layout: slides
title: "Classes and Objects"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>




</section>

<section markdown="block">
## Named Tuples


Defining a named tuple...

<pre><code data-trim contenteditable>
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
</code></pre>


Creating a named tuple

<pre><code data-trim contenteditable>
>>> p = Point(x=0,y=0)
>>> p.x
0
>>> p.y
0
</code></pre>

Another way of creating a named tuple

<pre><code data-trim contenteditable>
>>> q = Point(14, 16)
>>> q
Point(x=14, y=16)
</code></pre>
</section>

<section markdown="block">
## Named Tuples Continued

Accessing items

<pre><code data-trim contenteditable>
>>> q.x
14
>>> q[0]
14
</code></pre>

Unpacking

<pre><code data-trim contenteditable>
>>> x, y = q
>>> x
14
</code></pre>

Immutable!
<pre><code data-trim contenteditable>
>>> q[0] = 100
>>> // exception!
</code></pre>

</section>
<section markdown="block">
## Classes and Objects

Topics

* creating a class
* self
* methods (have self)
* __init__
* base class, multiple base classes
</section>
