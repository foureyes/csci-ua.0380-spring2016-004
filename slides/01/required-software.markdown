---
layout: slides
title: "Required Software"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Minimally, You'll Need...

* Python 3
* a text editor or an IDE


</section>
<section markdown="block">
##  Python 3

__The latest version of Python 3 is 3.5.x.__ 

* (It's likely that any version of Python 3 will work for our purposes, though)
* If you __don't already have Python 3 installed__...
    * [download and use the installer](https://www.python.org/downloads/)
    * (recommended) if you're comfortable using the commandline, and you're on OSX or Linux
        * OSX ... use [homebrew](http://brew.sh/), <code>brew install python3</code>
        * Ubuntu ... Python3 is probably already installed! 
        * (if not, use apt-get <code>sudo apt-get install python3</code>)

</section>

<section markdown="block">
## Text Editor / IDE

Use [PyCharm](https://www.jetbrains.com/pycharm/). Don't use IDLE.

1. Download the free __Community Edition__ (PyCharm CE)
2. Configure PyCharm to use Python 3 by [following these directions](https://www.jetbrains.com/pycharm/help/configuring-available-python-interpreters.html)

If PyCharm doesn't work for you, then...

* talk to me about using sublime and the commandline
* ...or use another editor / IDE that you're comfortable with
* ok, fine. IDLE.


</section>

<section markdown="block">
## Using PyCharm

PyCharm organizes your code by projects. I'd recommend using:

* 1 project per homework
* (or 1 project per class)
* creating a new file in that project for every separate file you need

Use the following commands:

* __Create a project:__ File &rarr; new Python File
* __Create a file:__ File &rarr; new &rarr; Python File
* __Run last file:__ Run &rarr; filename (control R also works for this)
* __Run specific file:__ Run &rarr; choose file name

</section>

<section markdown="block">
## Additional Stuff...

We'll take a look at the following tools in our next class:

* easy_install
* pip
* virtualenv

</section>
