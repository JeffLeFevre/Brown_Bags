__What Does a Context Manager do?__
+ Efficient resource management
+ Automatic resource tear-down
+ Reduction in code
+ Good error handling comes automagically
---
__What Does a Context Manager Look Like?__
+ Decorator-based
    1. Less code
    2. Not as clear to others reading your code
    3. Python contextlib library provides a contextmanager decorator.
    4. Decorators in general can be difficult for others to easily understand and troubleshoot.
   
+ Class-based:
    1. ```__init__```
    2. ```__enter__```: try/except, return resource
    3. ```__exit__```: behaves like a ‘finally’ - always called, close out resource, tie up loose ends.
    
+ The ‘with’ statement:
    1. Calls a built-in class or your custom class.
    2. Instantiates a Context Manager object
    3. Left indent ends the ‘with’ statement, calling ```__exit__()```
---
__How do you Test a Context Manager?__
+ Class-based method easier to test:   
    + Check that the appropriate methods are being called
    + Check resource state on ```__enter__()```
    + Check resource state on ```__exit__()```
    + Ensure errors thrown
    + Structure helps lay out appropriate use
---
__What are the Benefits to Using a Context Manager?__
+ Better error handling
+ Resources properly closed out in any scenario
---
__What are the Drawbacks?__
+ Code might not be as readable
+ Hammer and nail - be sure the library or built-in you’re using doesn’t   
  already have a context manager!
---
__Resources:__
https://docs.python.org/3/library/contextlib.html - Python 3.7 Context Manager Library
https://docs.python.org/3.6/library/contextlib.html - Python 3.6 Context Manager Library
https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/ - Thread lock example
https://medium.com/@ramojol/python-context-managers-and-the-with-statement-8f53d4d9f87 - Database and Requests library examples    
https://www.zeolearn.com/magazine/the-truth-about-context-managers-in-python
https://youtu.be/-aKFBoZpiqA - Context Manager tutorial video
