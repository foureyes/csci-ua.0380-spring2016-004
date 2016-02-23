---
layout: slides
title: "Paths, More File I/O, Data Formats and Sources"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Paths and open

Using __open__, if you just pass in a file name as the first argument, Python will look in the directory that _the program is running from_. 

The directory that your program is running from is the __current working directory__.

* in PyCharm, your project folder is your current working directory
* if you're running from the __commandline__, __whatever directory you're in__ is the current working directory

For example, in PyCharm, and your project is in:

<pre><code data-trim contenteditable>
/Users/myusername/PycharmProjects/my_amazing_project/
</code></pre>

<pre><code data-trim contenteditable>
f = open("data.txt", 'r')

# attempts to open this file:
# /Users/myusername/PycharmProjects/my_amazing_project/data.txt
</code></pre>

</section>

<section markdown="block">
## But, My File is Somewhere Else!

__You can specify a file out of your current working directory as well!__

There are two ways you can do this:

1. Use a path that's __relative__ to your current working directory
2. Use an __absolute__ path that will work regardless of what your current working directory is

__UH WAT?__ &rarr;

</section>

<section markdown="block">
## Relative Paths 

__Relative paths__ are paths specified relative to your current working directory

Without any prefixes, a file name on its own will refer to _that file_ in your current working directory. __you can also use the following to specify your relative path__ &rarr;

* __<code>./</code>__  - current working directory
* __<code>./dir1/dir2</code>__  - dir2 nested in dir1 in current working directory
* __<code>../</code>__ - go up one directory
* __<code>../../</code>__ - go up two directories
</section>

<section markdown="block">
## Relative Path Examples

Assume that your project folder is in:

<pre><code data-trim contenteditable>
/projects/cool_stuff/
</code></pre>

__Where will open look for the file?__ &rarr;
<pre><code data-trim contenteditable>
f = open("foo.txt", 'r')
f = open("./foo.txt", 'r')
f = open("../foo.txt", 'r')
f = open("../../foo.txt", 'r')
f = open("./hmmm/foo.txt", 'r')
</code></pre>

<pre><code data-trim contenteditable>
/projects/cool_stuff/foo.txt
/projects/cool_stuff/foo.txt
/projects/foo.txt
/foo.txt
/projects/cool_stuff/hmmm.foo.txt
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Absolute Paths

__Absolute paths__ will refer to the same file regardless of what your current working directory is. You can also think of them as based off of __root directory__

* __root__ is the top most directory in your file system
* on OSX, it's just <code>/</code> (and usually refers to something _like_ <code>Macintosh HD</code>)
* or on Windows, maybe it's <code>c:</code>
* an absolute path will start at __root (<code>/</code>)__

<pre><code data-trim contenteditable>
/projects/cool_stuff/foo.txt
</code></pre>

So you can do something like:

<pre><code data-trim contenteditable>
f = open('/projects/cool_stuff/foo.txt', 'r')
</code></pre>

</section>

<section markdown="block">
## File I/O Review

__(See slides from previous class for details)__

* __opening__ and __closing__
* reading a file
* methods for reading
    * iterate
    * read
    * readlines
    * readline (call consecutively)
* writing to a file

__One thing to note about closing your files though...__ &rarr;
</section>

<section markdown="block">
## Using a Context Manager

__Always close__ your file when you're done working with it... but what if there's an exception? <code>try/except/finally</code> works... but <code>with</code> is better. It'll automatically close any time the with expression's block is exited!

<pre><code data-trim contenteditable>
with expression as variable
    use variable
</code></pre>

<pre><code data-trim contenteditable>
with open('myfile.txt') as f:
    for line in f:
        print(line)
</code></pre>

__Prefer using <code>with</code> rather than simply using <code>open</code> and <code>close</code> explicitly__.
</section>


<section markdown="block">
## File Formats

We're reading text files for now. They can come in a multitude of formats. __Why do we care?__ &rarr;

__Format determines how we extract meaningful data from a file.__ &rarr;
{:.fragment}

Yeah... great, reading files is fun and all, but it's all just a bunch of nonsense if we don't know how it's formatted, right? __What are some common text file formats?__ &rarr;
{:.fragment}

* _just text_ ... like files from project gutenberg / no standard format
* __csv__ or value separated (can have other delimiters!)
* __fixed width__
* __markdown__
* __html__
* __xml__
* oh... also json
{:.fragment}
</section>

<section markdown="block">
## Ok... How do We Deal With Diff Formats?


* text ... just read it in, that's about as good as you can do
* __csv__, split (or...)
* __fixed width__, slice maybe?
* __markdown__, uh-oh
* __html__, uh-oh
* __xml__, uh-oh
* oh... also json

We'll need to bring in some more robust tooling for those last few.

</section>

<section markdown="block">
## The Problem With csvs

csvs seem fine. That is until... __What's tricky about using split with csvs?__ &rarr;


sometimes pesky commas are legit characters
{:.fragment}

Wait, did you know there's actual an [RFC for CSVs (like a _standard_ specification for what CSV actually is)](https://tools.ietf.org/html/rfc4180.html)
{:.fragment}
</section>

<section markdown="block">
## csv module

Ok... that seems complicated enough. __Let's not write that ourselves. That's where the csv module comes in__. &rarr;

1. Basically... you create a __reader object__
2. And you just __loop over it__
3. Each row is a __list of strings__ (regardless of content)
4. CSV MODULE FTW! (commas in quotes, no problem)

[Note that the docs on this show that you can do things like:](https://docs.python.org/3/library/csv.html#module-contents)

* can specify the _dialect_ (for example there's a specific way that Excel creates csvs)
* change delimiter
* change quote char, etc.
</section>

<section markdown="block">
## csv module continued

__Let's take a look at using the csv module...__ &rarr;
<pre><code data-trim contenteditable>
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print(row[0])
</code></pre>

* notice that the reader object is created by calling <code>csv.reader</code> and passing in a file object
* from there, simply loop (printing the whole row shows it's a list...)
</section>

<section markdown="block">
## Wanna Get Fancy, Do Ya?

__How about reading those rows as dictionaries instead?__ First row is considered the keys (they should be the headers, right?).

<pre><code data-trim contenteditable>
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print(row['pace'])
</code></pre>
</section>

<section markdown="block">
## Fixed Width

__Ok... slicing seems like it's no problem. Right? NBD.__

* reading fixed width seems to be straightforward
* just slice per width specified
* don't forget to strip any excess spaces, though!

Writing to a fixed with file has one minor wrinkle, though. __What is it?__ &rarr;

* {:.fragment} some data may be longer than the _actual width_ allowed in your fixed width fields
* {:.fragment} if that's the case the data will have to be truncated (shortened, with the excess part being lopped off!)
* {:.fragment} some data may be shorter than the _actual width_ ... in which case, the data would have to be padded


</section>

<section markdown="block">
## Markdown, HTML, XML, JSON

Ok... now we're getting into some formats that aren't really column based. HTML, XML and JSON are all kind of hierarchical. __You don't want to mess with these on your own. It's actually quite difficult to get exactly right.__ &rarr;

* some liken it to dealing with Lovecraftian elder gods!
* [check out the classic stack overflow answer](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)
* it also likely means you'll have to use lots of complicated regular expressions
* [...and, of course, regular expressions: now you have two problems](http://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)


</section>

<section markdown="block">
## So How Do We Even?

Find someone that already went through the pain of doing it, and use their library.

For HTML, a commonly use library is beautiful soup 4:

[bs4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


</section>


<section markdown="block">
## Beautiful Soup 4

Here's a quick demonstration of how BeautifulSoup works...

<pre><code data-trim contenteditable>
from bs4 import BeautifulSoup

dom = BeautifulSoup("""
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;foo&lt;/h1&gt;
&lt;p&gt;bar
&lt;h1 class='even-headier'&gt;baz&lt;/h1&gt;
&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
""", "lxml")
</code></pre>
<pre><code data-trim contenteditable>
print(dom.select('h1'))
print(dom.select('.even-headier'))
</code></pre>
</section>


<section markdown="block">
## JSON

Aaaand. Lastly, JSON. __Use the <code>json</code> module to convert to and from Python dictionaries and JSON strings__ &rarr;

<pre><code data-trim contenteditable>
import json
# dumps <-- creates a string from a python dict... as json format
# loads <-- reads a string into a python dict (assuming string is json)

s = '{"first":"joe", "last":"versoza"}'
d = json.loads(s)
print(d)
</code></pre>

</section>
<section markdown="block">
## Where Data is Sourced From

Now that we're set with file formats, __let's figure out where we source data from__ &rarr;

* __locally__ (on your file system)
    * use open
* __remotely__... on some other server
    * use requests
    * or urllib
        * download first
        * or read directly as string


</section>

<section markdown="block">
## Which One to Use???

__So... how do you decide whether or not to download and save from a remote server or read and process immediately?__ &rarr;

* {:.fragment} too big to fit in memory? save first
* {:.fragment} ...or stream the data (requests allows this)
* {:.fragment} if the data changes often:
    * {:.fragment} and you need _live_ data, then read from server and process
    * {:.fragment} but if you need consistent data across a set of all data, maybe download and save first?
* {:.fragment} also, you may want to limit how often you request data (some sites have limits on this)
* {:.fragment} if it's processor intensive, or large batches of data... maybe it makes sens architecturally to separate downloading from processing

</section>

<section markdown="block">
## Getting Data from a URL

Using the requests module to __retrieve data from a url__ &rarr;

<pre><code data-trim contenteditable>
import requests
res = requests.get("http://cs.nyu.edu")
print(res.status_code) # http response status code (you want a 200)
print(res.text) # the contents / body of the response
</code></pre>
</section>

<section markdown="block">
## Requests and json

The requests module does json parsing for you!

<pre><code data-trim contenteditable>
res = requests.get("http://data.nba.com/data/15m/json/cms/noseason/game/20160221/0021500824/boxscore.json")

j = res.json()
print(j)
</code></pre>
</section>


{% comment %}
<section markdown="block">
## Creating an Image

<pre><code data-trim contenteditable>
from PIL import Image

img = Image.new( 'RGB', (255,255), "black") # create a new black image

pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show()
</code></pre>

</section>

<section markdown="block">
## Turn this wallaby black and white?

<pre><code data-trim contenteditable>
img = Image.open('wallaby.jpg')

</code></pre>
</section>
{% endcomment %}
