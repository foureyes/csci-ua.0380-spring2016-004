---
layout: slides
title: "Introductions"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<small style="text-align:center; display:block" markdown="block">
	__(By the way, I'm Joe Versoza.__  😀👋 __)__
</small>

</section>

<section markdown="block">
## Are You in the Right Classroom?

<h3 class="fragment">
Maybe ¯\_(ツ)_/¯
</h3>

<div class="fragment"  markdown="block">
* this is __{{site.course_number}}-{{site.course_section}}__
* {:.fragment} hm... that's just a bunch of random letters and numbers, what is this really?
* {:.fragment} __{{site.course_name}}__
</div>
</section>

<section markdown="block">
# HI!

</section>

<section markdown="block">
## A Quick Introduction

I'm __Joe Versoza__

* Clinical Assistant Professor in the Computer Science Department
* email: jversoza at cs dot nyu dot edu
* you can find me in {{site.office_hours_room}}during my office hours... 
* {{site.office_hours}}

Um. Some of you already know me!

* {:.fragment} (Why would you want to be in _another_ class with me???)
* {:.fragment} Big MISTAKE! 😂 😕 
</section>

<section markdown="block">
## Some Things About You...

* {:.fragment} you're a __web programming minor__ ...
    * {:.fragment} or you're interested in _intermediate_ Python
* {:.fragment} you've already taken __Introduction to Computer Programming__... 
    * {:.fragment} or maybe you're a self-taught __Pythonista__ 🐍🐍🐍 
    * {:.fragment} Pythonista? <span class="fragment">(someone that writes Python programs, probably sourced from [this article](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)!</span>
* {:.fragment} lastly, you may or may not have __taken 0004 (web design)__
    * {:.fragment} but that doesn't matter ...
    * {:.fragment} there's only a couple of topics that require HTML and CSS, and it's easy to pick up

</section>

<section markdown="block">
# About This Class

</section>
<section markdown="block">
## Some Background

<span markdown="block" style="text-align:center; display:block;">
This is the __first time__ this class is being offered!
</span>

* {:.fragment} sooo... it'll be pretty _rough around the edges_ (excuses, excuses!)
* {:.fragment} __raise your hand if you're a cs major__ &rarr;
    * {:.fragment} this class was originally intended for __non__ majors 
    * {:.fragment} you'll find that there's some __overlap with 101__, as well as other classes you may have taken! 
    * {:.fragment} (but hopefully, we'll augment what you already know)

</section>

<section markdown="block">
## Python for Applications

What is this class actually about? 

__We're going to go cover...__ &rarr;

* intermediate Python topics
* ...and see how we can use them for problem solving in various application domains

</section>


<section markdown="block">
## Applications

__Roughly in this order...__ &rarr;

* {:.fragment} graphics and animation
* {:.fragment} basic numerical analysis and statistics
* {:.fragment} data retrieval and processing
* {:.fragment} simple cryptographic algorithms
* {:.fragment} an introduction to image processing
* {:.fragment} creating _simulations_ (astronomy, ecosystems)
* {:.fragment} simple machine learning and data mining applications
* {:.fragment} networking (servers and clients)
* {:.fragment} a small web application
* {:.fragment} an intro to digital signal processing (audio)
* {:.fragment} sensor input
* {:.fragment} a small game

</section>

<section markdown="block">
## Python Topics

__We'll cover the following Python related topics...__ &rarr;

* {:.fragment} __Basics__ (this'll be quick!)
* {:.fragment} __Compound_ Types__ (Sets, Tuples, Dictionaries, etc.)
* {:.fragment} __Input and Output__ (File IO, Networking, Web)
* {:.fragment} __Tools for Creating Abstractions__
    * {:.fragment} Functions, Decorators, Higher Order Functions
    * {:.fragment} Classes and Inheritance, Context Managers
    * {:.fragment} Iterators and Generators (Interfaces)
* {:.fragment} __Various Libraries__ (maybe matplotlib, CImage, scikit-learn, flask, requests, etc.)
* {:.fragment} <strong markdown="block">_Development_ Tools</strong>
    * {:.fragment} applications for writing and debugging programs (IPython, PyCharm, pylint, pdb, etc.)
    * {:.fragment} module / package management (pip, virtualenv, etc.)

</section>

<section markdown="block">
## Readings / Books

So... __I'm _actually_ assigning readings__... about one set every week. &rarr;

* [{{ site.book1 }}]({{ site.book1_link }}) by {{ site.book1_author }}
* [{{ site.book2 }}]({{ site.book2_link }}) by {{ site.book2_author }}
* and the [Official Python 3 Docs](https://docs.python.org/3/)

The reading will complement the following week's lectures.

* (so you should read them before class)
* (and if you need more motivation to do the readings...)
</section>

<section markdown="block">
## Online Quizzes

This may be ambitious on my part, but I'll try to create an __online quiz__ for each assigned reading.

* you'll find the quizzes on __NYU classes__
* they'll be __due about a week after the readings are assigned__
* they should be fairly straightforward
    * multiple choice, short answer
    * automatically graded
    * multiple submissions allowed (max 5, last score recorded)
    * based on assigned readings

</section>

<section markdown="block">
## Yes, There Will be Exams

__Midterm__ (there's only one)

* {{ site.midterm1_date }}
* {{ site.midterm1_time }}

__Final__

* {{ site.final_date }}
* {{ site.final_time }}
* {{ site.final_room }}

<br> 

<div class="fragment"> (Clearly, I'm not the person that schedules final exams)</div>

</section>

<section markdown="block">
## In Class Assignments / Activities

We'll _occasionally_ have __in-class activities__ &rarr;

* {:.fragment} surveys, open book quizzes, and small programming exercises
* {:.fragment} I'll give you at least a week lead time, so you'll make sure to attend
* {:.fragment} (but you'd be coming to every class anyway, though... right? :P)

</section>

<section markdown="block">
## Homework

There will be about __8 or 9 homework assignments__.

* Turned in __electronically__ via __NYU Classes__, usually __due one week after posting__
* The assignment will __stay open up to 24 hours in NYU classes__
	* After the 24 hour grace period, homework cannot be submitted
	* A pattern of late homework will result in zero points for the next late homework (even if submitted within he 24 hour grace period)
* The last couple of homeworks will be shorter compared to the others because you'll also be working on a final project (more on that later)

</section>

<section markdown="block">
## Homework Policy

__Do your own work; don't plagiarize code / cheat.__ Please read the [page on academic integrity](http://www.cs.nyu.edu/webapps/content/academic/undergrad/academic_integrity)

* You can help fellow students debug or discuss high-level algorithms
* __But write your own code!__ (don't copy other students' work, solutions found online, etc.)
* Cases of plagiarism are sent to the Director of Undergraduate Students

</section>

<section markdown="block">
# Oh hey. Write your own code!

<small style="text-align:center; display:block" markdown="block">
	__(Did I say that already? Seriously, though - don't copy other students' work.)__
</small>
</section>

<section markdown="block">
## Final Project and Presentation

__A final project and presentation are due at the end of the semester.__ &rarr;

* it should initially be assigned just after spring break
* full details tbd, but...
    * most likely, the project will require the use of some number of modules or topics that we learned / will learn in class
    * the presentation will demonstrate your understanding of the work that you put into the project (it'll probably be 2 or 3 minutes max)

</section>

<section markdown="block">
## Grading

__How does that all fit it in to your final grade?__  &rarr;

* __20%__ - Homework
* __5%__ - Online Quizzes 
* __5%__ - In-Class Activities
* __25%__ - Midterm
* __30%__ - Final Exam
* __15%__ - Final Project
</section>
<section markdown="block">
## Getting Help

* see me right __before or after class__! 
* drop by my __office hours__ ({{ site.office_hours_room }}): {{ site.office_hours }}
* email me at __{{ site.email }}__
    * {:.fragment} __if I don't get back to you within 48 hours__
	    * {:.fragment} I wasn't able to get to your email yet
	    * {:.fragment} robots think your email is shady
	    * {:.fragment} my inbox exploded
    * {:.fragment} ... so you should __email me again__, or better yet, __see me in person__
</section>

<section markdown="block">
## As I Promised

(Now for a quick survey)

* [Python for Applications Survey](https://docs.google.com/a/nyu.edu/forms/d/108t13HKoAZiKmdGbdroosVKIpXL9E6ehq_OTdpVsTpI/viewform)
* (you'll need to log in with your netID)
* (raise your hand if you don't have a laptop and internet access; I'll give you a paper version!)

</section>
{% comment %}
{% endcomment %}


{% comment %}
<section markdown="block">
## Topics

* Python Overview
* Setup
* Basic Control Structures
* Functions
* turtle module
* random module

</section>
<section markdown="block">
## An Embed


embedding stuff here

yaass!

<iframe src="https://trinket.io/embed/python/d862d96bd7?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

</section>

<section markdown="block">
## Aced

<div>
<div data-editable markdown="block">
x = 5
for i in range(x):
    print("foo")
</div>
</div>

</section>

<section markdown="block">
## Aced Pt 2

<div>
<div data-editable markdown="block">
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.forward(400)
wn.mainloop()
</div>
</div>
</section>

<section markdown="block">
## Styles

### an h3

#### an h4

<aside>...And an aside</aside>

* [A link](http://www/nyu.edu)
* __Bold__, but not bold
* _italics_, but not italics

</section>

<section markdown="block">
## Some Code

<pre><code data-trim contenteditable>
def do_stuff(a, b="stuff"):
    print("hello")
    new_list = []
    for i in range(5):
        if i == 2:
            new_list.append(i)
    return new_list
</code></pre>

</section>

<section markdown="block">
## Python Overview


* turtle

* readings
</section>
{% endcomment %}
