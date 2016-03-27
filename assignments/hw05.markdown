---
layout: homework
title: "Assignment #5"
---

<style>
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}
</style>

# Assignment #5 - Due Friday, April 1st

* __Part 1__ readings
* __Part 2__ decorated.py 
* __Part 3__ quizzical.py
* __Part 4__ gravity.py

## Part 1 - Readings

#### From our Book

Read __Chapter 10 (Astronomny)__ in {{ site.book1 }}.  This chapter provides information on classes and objects.


#### Online Resources

* You'll need to use [a special keyword, nonlocal, in a couple of the functions you create... read about it in this article](https://www.smallsurething.com/a-quick-guide-to-nonlocal-in-python-3/)
* In addition to the slides: 
    * read this [article on decorators](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
    * or this article [article on more advanced decorator usage](http://thecodeship.com/patterns/guide-to-python-function-decorators/)
* You'll need to use the csv module for part 3, so [check out the documentation on it](https://docs.python.org/3/library/csv.html)
* You'll have to use custom exceptions (which are provided for you) in part 3; read the official Python 3 documentation on [raising exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) and [creating custom exceptions](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)
* Python has a [bunch of magic methods, which are detailed in this guide](http://www.rafekettler.com/magicmethods.html)
     

## Part 2 - decorated.py

At first glance, decorators seem a little tricky, but once you write a few of them, a pattern emerges. Try creating the decorators specified in the requirements below.

#### Setup

1. Download [decorated.py](hw05/decorated.py) - place your decorators in this file
2. [test_decorated.py](hw05/test_decorated.py) - test your code in this file

#### Technical Requirements

Write the following decorators in your <code>decorated.py</code> file:

1. <code>debug</code>
2. <code>limit_one_call</code>
3. <code>count</code>
4. <code>limit_calls</code> (extra credit) 

Once you're done, try running <code>test_decorated.py</code> in the same directory. It will verify that your decorators are named correctly, and it will show the output of using all of the decorators you implemented, regardless of whether or not you implemented the extra credit, <code>limit_calls</code>.

As you develop each decorator, you can test by placing your own test code in within an <code>if __name__ == '__main__'</code> block in <code>decorated.py</code>

#### Debug

The <code>debug</code> decorator will add debugging print statements to an existing function. These debug statements will print out all of the values and types of the arguments passed in as well as the returned value. 

* Each argument will be printed out in the form, <code>argument (number): (value), (type)</code>, where number is the positional number of the argument (1 would be the first argument passed in), value is the value of the argument, and type is the type of the argument as returned by the <code>type</code> function. 
* After the number of arguments are printed out, the original function is called... and the return value is printed out along with its type, in a format similar to the arguments: <code>return: (value), (type)</code>.
* For example, if we replaced the built-in function <code>min</code> with a version decorated with <code>debug</code>, calling <code>min(5, -2, 4)</code> would print out the following:
    <pre><code data-trim contenteditable>argument 1: 5, <class 'int'>
argument 2: -2, <class 'int'>
argument 3: 4, <class 'int'>
returns: -2, <class 'int'>
</code></pre>

#### limit_one_call

The <code>limit_one_call</code> decorator will ensure that a function decorated with it can be called only once for the lifetime of your program. Any subsequent calls to the decorated function will not execute the function (and consequently, no value, or <code>None</code>, will be returned rather than the actual result of calling the function).

* __You will have to use the keyword, <code>nonlocal</code>, to implement this decorator.__ <code>nonlocal</code> is similar to <code>global</code>, but instead of affected global identifiers, it affects variables in a scope that encloses the current scope. [Please read this article on how to use <code>nonlocal</code>](http://stackoverflow.com/questions/1261875/python-nonlocal-statement).
* An example of using the <code>limit_one_call</code> decorator is to replaced the built-in <code>print</code>function with a <code>limit_one_call</code>decorated version of it. This code:
    <pre><code data-trim contenteditable>limited_print = limit_one_call(print)
limited_print('hello')
limited_print('howdy')
limited_print('hola')
</code></pre>
    Would only print out <code>hello</code> once! The output would be:
    <pre><code data-trim contenteditable>hello
# notice that howdy and hola *won't be printed*
</code></pre>

#### count

The <code>count</code> decorator will print out the number of times that a function decorated with it is called. This will be pretty similar to the previous decorator, <code>limit_one_call</code> in that __you'll have to use the keyword, <code>nonlocal</code>, to implement it.__ Again, [please see this stack overflow article to on how to use <code>nonlocal</code>](http://stackoverflow.com/a/309000). 

* The format of the output of a decorated function is simply: <code>function has been called (number) times</code>
* For example, the following code uses the <code>count</code> decorator to create a decorated version of the built-in <code>print</code>:
    <pre><code data-trim contenteditable>counted_print = count(print)
counted_print('hello')
counted_print('howdy')
counted_print('hola')
</code></pre>
    Would print out:
    <pre><code data-trim contenteditable>hello
function has been called 1 times
howdy
function has been called 2 times
hola
function has been called 3 times
</code></pre>

#### limit_calls (extra credit)

For __extra credit__, write a decorator called <code>limit_calls</code>... which is essentially a heavily modified version <code>limit_one_call</code>. Instead of limiting to a single call, the number of calls of the limit will be specified on every use of the decorator (parameterized). In addition to that functionality, you'll also add some features that make for a more _properly_ constructed decorator.

The code below shows how the <code>limit_calls</code> decorator could be used:

<pre><code data-trim contenteditable>@limit_calls(2)
def say_hi_to_everyone(*args, greeting='hello'):
    """returns string consisting of greeting and arg for 
    every argument passed in
    """
    return '\n'.join(['{} {}'.format(greeting, name) for name in args])
</code></pre>

The code above...

1. limits the number of calls to <code>say_hi_to_everyone</code> to 2 (notice that limit_calls is parameterized)
2. allows keyword args to be passed into the decorated function
3. ensure that attributes of the function object, <code>say_hi_to_everyone</code>, are transferred to the replaced one:
    <pre><code data-trim contenteditable>print(say_hi_to_everyone.__name__)
print(say_hi_to_everyone.__doc__)
</code></pre>

To do this, you'll need to do a __a bit of additional reading__. [Read this guide to function decorators from thecodeship.com](http://thecodeship.com/patterns/guide-to-python-function-decorators/). It covers:

* passing arguments into decorators (a function that returns decorators... wait, what!?!?)
* handling keyword arguments that are passed into the decorated function
* using functools.wraps (for more info on functools.wraps, [check out the obligatory stack overflow article](http://stackoverflow.com/questions/308999/what-does-functools-wraps-do/309000#309000) because the official docs aren't quite adequate for explaining it

#### Testing decorated.py

Finally, when you're done with implementing and testing <code>decorated.py</code>, __run the test code in <code>test_decorated.py</code>__.

Its output should be (ignore the last part if you did not do the extra credit):

<pre><code data-trim contenteditable>###########################
# TESTING DEBUG DECORATOR #
###########################
argument 1: [1, 2, 3], <class 'list'>
argument 2: hello, <class 'str'>
argument 3: False, <class 'bool'>
returns: bar, <class 'str'>

argument 1: 99, <class 'int'>
argument 2: 100, <class 'int'>
returns: 100, <class 'int'>

####################################
# TESTING LIMIT_ONE_CALL DECORATOR #
####################################
calling decorated say_hello 0, output is:
hello
calling decorated say_hello 1, output is:
calling decorated say_hello 2, output is:

###########################
# TESTING COUNT DECORATOR #
###########################
function has been called 1 times
function has been called 2 times

function has been called 1 times
function has been called 2 times

################################################
# TESTING LIMIT_CALLS DECORATOR (EXTRA CREDIT) #
################################################
value in __name__: say_hi_to_everyone
value in __doc__: returns string consisting of greeting and arg for
        every argument passed in

call 1
-----
hi alice
hi bob

call 2
-----
hi alice
hi bob

call 3
-----
None

</code></pre>

## Part 3 - quizzical.py

Write two classes: 

1. <code>MultipleChoiceQuestion</code> - represents a questions with a list of potential answers, with exactly one answer being correct
2. <code>Quiz</code> - represents a series of multiple questions that can be displayed in random order for an interactive quiz

Once you've created the two classes, read a <code>.csv</code> file that contains questions and run an interactive quiz based on those questions.

#### Setup

1. Download [quizzical.py](hw05/quizzical.py) - contains <code>MultipleChoiceQuestion</code> and <code>Quiz</code>
1. Download [python_quiz.py](hw05/python_quiz.py) - this uses the classes above to run an interactive quiz (should only be a few lines long!)
2. Download [questions.csv](hw05/questions.csv) - source of questions for quiz

#### Technical Requirements

You'll be create 2 classes and a program that utilizes both of your classes. See the requirements below.

#### MultipleChoiceQuestion

<code>MultipleChoiceQuestion</code> objects represent a question that has a list of potential answers, with only one answer being correct. You'll only need to implement the features specified below; any other corner cases, boundary conditions, etc. will not be graded, but feel free to implement, as there are many scenarios not outlined in these requirements.

A <code>MultipleChoiceQuestion</code> contain the following data:

1. the text of the question
2. all of the choices that could be potential answers to the question, and their corresponding label, a letter, lowercase a through z
3. the letter of the correct answer

<code>MultipleChoiceQuestion</code> should support the following methods:

1. a __constructor__ that takes the question text as an argument
    * the question text is only the question itself, not the list of choices
    * a newly created question will have <code>None</code> initially set as its answer
    * it will not have any choices to begin with
    * example usage:
        <pre><code data-trim contenteditable>q1 = MultipleChoiceQuestion('Which type is immutable?')
# no choices, None as answer...
</code></pre>
2. <code>add_choice(self, letter, text)</code> - adds a choice to a question: letter is the label for the choice, text is the actual text representing the choice
    * no return value
    * example usage (adds 3 choices, a, b, and c, to the question created):
        <pre><code data-trim contenteditable># adds three choices to question, q1...
q1 = MultipleChoiceQuestion('Which type is immutable?')
q1.add_choice('a', 'list')
q1.add_choice('b', 'tuple')
q1.add_choice('c', 'dict')
    * if the letter is not a lowercase letter from <code>a</code> through <code>z</code>, raise an <code>InvalidCharacterError</code> exception (this <code>Exception</code> class is already defined for you in <code>quizzical.py</code>
    * see [the docs on raising an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) to implement this part
    * an example of causing this exception is:
    <pre><code data-trim contenteditable>try:
&nbsp;&nbsp;&nbsp;&nbsp;q1.add_choice('!', 'pizza')
except InvalidCharacterError as e:
&nbsp;&nbsp;&nbsp;&nbsp;print('{}:{}'.format(e.__class__.__name__, e))
</code></pre>
3. <code>set_choices(self, all_choices)</code> - sets all of the questions to the text in a list of choices
    * no return value
    * the letter labels are  automatically generated based on the position of the choice in the list (position 0 will be choice a, position 1 will be choice b, etc.)
    * example usage (instead of adding 3 choices individually, adds 3 choices in a list):
        <pre><code data-trim contenteditable>q1.set_choices(['list', 'tuple', 'dict'])
</code></pre>
4. <code>set_answer(self, letter)</code> - sets the letter of the answer to this question
    * no return value
    * example usage:
        <pre><code data-trim contenteditable>q1 = MultipleChoiceQuestion('Which type is immutable?')
q1.add_choice('a', 'list')
q1.add_choice('b', 'tuple')
q1.add_choice('c', 'dict')
q1.set_answer('b')
</code></pre>
    * if the character is not an answer that has already been set, raise a <code>ChoiceDoesNotExistError</code>:
        <pre><code data-trim contenteditable>q2 = MultipleChoiceQuestion('What is your favorite color?')
try:
&nbsp;&nbsp;&nbsp;&nbsp;q2.set_answer('a')
except ChoiceDoesNotExistError as e:
&nbsp;&nbsp;&nbsp;&nbsp;print('{}:{}'.format(e.__class__.__name__, e))
</code></pre>
5. <code>is_correct_answer(self, letter)</code> - determines whether or not the given letter is the correct answer to this question
    * returns true or false... depending on whether or not letter passed in is answer set as correct answer for question
    * example usage:
        <pre><code data-trim contenteditable>q1 = MultipleChoiceQuestion('Which type is immutable?')
q1.add_choice('a', 'list')
q1.add_choice('b', 'tuple')
q1.add_choice('c', 'dict')
q1.set_answer('b')
# the following will print False
print('is a correct? ', q1.is_correct_answer('a'))
# the following will print True
print('is b correct? ', q1.is_correct_answer('b'))
</code></pre>
6. a __string representation__ of this question
    * when a <code>MultipleChoiceQuestion</code> object is printed out...  its string representation should be in the following format:
        * question, <code>Which type is immutable?</code>
        * separator, 5 <code>=</code>'s: <code>=====</code>
        * letters and choices, <code>a. list</code>
    * example output:
        <pre><code data-trim contenteditable>Which type is immutable?
=====
a. list
b. tuple
c. dict
</code></pre>

#### Quiz

A <code>Quiz</code> object represents a series of multiple choice questions. It can load questions from a file... and it can present its questions as an interactive application, with each question displayed, and the user prompted for an answer.

A <code>Quiz</code> object contains the following data:

1. a list of questions
2. (that's it, really!)

<code>Quiz</code> should support the following methods:

1. a __constructor__ - does not have any arguments (except for self, of course!)
    * initializes its list of questions
    * example usage:
        <pre><code data-trim contenteditable>quiz = Quiz()
</code></pre>
2. <code>add_question(self, question)</code> - adds a single question to this quiz object; a question is an instance of <code>MultipleChoiceQuestion</code>
    <pre><code data-trim contenteditable># first create a question
q1 = MultipleChoiceQuestion('Which type is immutable?')
q1.add_choice('a', 'list')
q1.add_choice('b', 'tuple')
q1.add_choice('c', 'dict')
q1.set_answer('b')
# then... add that question to the quiz
quiz.add_question(question)
</code></pre>
3. <code>load_questions_from_file(self, file_name)</code> - takes a single argument, a file name, and loads questions from that file
    * a csv of questions will have the following fields:
        1. the question text
        2. the letter of the answer
        3. the remaining fields are the text of the four answer choices, a, b, c, and d
    * see the [questions.csv](hw05/questions.csv)
    * note that __it has a header__
    * also note that __some fields have commas as part of the value__!
    * __use the csv module to read in this file__, either as...
        1. a [dictionary using the csv module's dictionary reader](https://docs.python.org/3/library/csv.html#csv.DictReader)
        2. or as a [list using the csv module's default reader](https://docs.python.org/3/library/csv.html#csv.reader)
    * example usage:
        <pre><code data-trim contenteditable>quiz.load_questions_from_file('../code/p4a-class15/questions.csv')
</code></pre>
4. <code>run_interactive_quiz(self)</code> - this method runs an interactive quiz 
    * It should:
        1. display each question, one at a time
        2. for every question...
        3. ask the user to choose an answer
        4. output whether or not the answer is correct
        5. ask the user to press return (just ask for input without saving the result of the input: <code>input('please press return/enter to continue')</code>)
        6. go on to the next question
        7. ... at the end, print out how many the user got right
    * example usage:
        <pre><code data-trim contenteditable>quiz.run_interactive_quiz()</code></pre>
    * example output/interaction (everything after <code>></code> is user input):
        <pre><code data-trim contenteditable>1. What does the @staticmethod decorator allow?
=====
a. allows a method to be called from the class only
b. allows a method to be called from an instance only
c. allows a method to be called from both an instance and the class
d. prevents a method from being called from both an instance and a class
&nbsp;&nbsp;
Please enter your answer
> b
NOPE... the answer was c
Press &lt;return&gt; to go to the next question
.
.
.
You got 3 / 4 correct.
</code></pre>

#### Running Your Quiz

In <code>python_quiz.py</code>:

1. import the module that contains your classes
2. use your <code>Quiz</code> class to create a <code>Quiz</code> object
3. load the <code>questions.csv</code> file (which you should have downloaded and placed into your project directory)
4. run the interactive quiz!
5. (um... there are only a few questions; I bet you can get them all right!)

## Part 4 - gravity.py 

Create an animation showing planets orbiting the sun. 

#### Setup

1. Download [gravity.py](hw05/gravity.py)

#### Technical Requirements

Sooo... you'll be creating the animation below; it simulates a couple of planets orbiting a sun:

![prr](../resources/img/hw05-orbit.gif )

1. Use the <code>turtle</code> module for your animation
2. Your implementation __must contain at least two classes__
3. Minimally, have __two planets orbiting the sun__
4. You can design these classes any way that you like in order to implement the animation
5. In this homework, it's ok to __derive most of your work from the book example__
    * chapter 10 guides you through creating a few classes and creating an animation based on those classes
    * __pay attention to the formulas__ used in chapter 10, in the part describing Animating the Solar System
    * <span class="warning">you'll have to adjust the program shown in the book</span> so that it it animates using <code>ontimer</code>
6. Of course, you don't have to follow the book... the implementation in the screen capture uses two classes:
    * a <code>Planet</code> class
    * a <code>Vector</code> class that implements vector functions, such as add, subtract and multiply
    * (probably a good exercise if you want to practice implementing some magic methods, like <code>__add__</code>)
7. (again, though, implement this however you like, as long as you have two classes and use them!)
8. It may be tricky to set up the right numbers for gravity, mass, and initial velocity of planets, so <span class="warning">if you're having trouble getting an orbit to catch, it's adequate to have the planets pass by and be thrown off orbit!</span>




