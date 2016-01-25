---
layout: slides
title: "Python Overview"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## variables, assignment, name space, object space

* __what are objects__?
    * a bundle of data and a actions 
    * more specifically...
    * have an id (never changes)
        * consider as a location in memory
        * is compares identity
        * id funciton returns
    * have a value (may change)
    * have a type (determines operations and methods)
* __naming objects... vs literals__
    * object space
    * name space
* __dot notation__

</section>

<section markdown="block">
## types

About types...

* __type == class__
* __mutability and immutability__
* __determines what you can and can't do w/ an object__
* __type function__

Types of Types

* __numeric types__
    * operations
* __compound types__
    * sequence types
        * operations
        * indexing, repetition, concatenation, slicing
        * del
    * mapping types
</section>

<section markdown="block">
## Bools and Functions

* __bools__
    * comparison operators
    * logical operators
* __functions__
    * also an object
    * function call _operator_
    
</section>

<section markdown="block">
## control structures

* __conditionals__ (no switch, though!)
* __loops__
    * while (with else?)
    * for, with iterable objects
        * range
        * sequence types
* __exception handling__

</section>

<section markdown="block">
## functions
* callable objects!
* calling functions
* user-defined functions, built-in functions, methods of built-in objects, class objects, methods of class instances, and all objects having a __call__() method are callable
    * https://docs.python.org/3.5/reference/expressions.html#calls

</section>
<section markdown="block">
## built-in functions

* (actually constructors) str, float, int, etc.
* print
* len
* type
* chr
* ord
* input
</section>

<section markdown="block">
## Creating Functions, Parameters and Arguments

* __defining a function__
* __positional vs keyword__
* __multiple args__
    * \*args
* __keyword arguments__
    * defining
    * passing
    * \*\*kwargs

</section>
<section markdown="block">
## Higher Order Functions, Scope

* __scope__
* __global__
* __nonlocal__
* __returning functions__
</section>

