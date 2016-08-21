# vclimbhelper
Installation
---------------
Aug 21, 2016
Version: 0.01

Code tested using Python 2.7.10

Install the following Python packages:
* [pip] (http://pypi.python.org/pypi/pip)
* [distribute] (http://pypi.python.org/pypi/distribute)
* [nose] (http://pypi.python.org/pypi/nose/)
* [virtualenv] (http://pypi.python.org/pypi/virtualenv)

Run
-----
```
$ nosetests -s
```

All tests must pass. Expected last few lines of output
```
----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
```

Sample usage
--------------
```python
tracer = Tracer()
#
# methods of interest
#
tracer.set_trace_methods(['method1', 'method3'])
tracer.start()

#
# Now, call the target method(s) of interest
#

method1()
method3()

# Then (optionally) call one or more of these:
#   get_calllist_iterator
#   get_returnlist_iterator
#   get_exceptionlist_iterator
#

# Optionally print using tracer.printStats()
tracer.printStats()

# Finally, reset 
tracer.reset()
```


Sample Output (using printStats())
------------------------------------
```
### Called Methods ###
{'func_name': 'method1', 'func_filename': '/Users/vmullachery/mine/NYU/summer2016/IndStudy/lpthw/vclimbhelper-oo/tests/calltrace_tests.py', 'func_line_no': 15}
{'func_name': 'method3', 'func_filename': '/Users/vmullachery/mine/NYU/summer2016/IndStudy/lpthw/vclimbhelper-oo/tests/calltrace_tests.py', 'func_line_no': 21}
### Method Return Values ###
{'func_name': 'method1', 'return_value': 'Hello, World!'}
{'func_name': 'method3', 'return_value': None}
### Method Exceptions ###
{'func_name': 'method3', 'exception_name': 'RuntimeError', 'exception_value': RuntimeError('Error raised in method3',), 'func_line_no': 22}

```

Output interpretation
-----------------------
1. Called methods
  * method1 on line 15 of specified file called
  * method3 on line 21 of specified file called

2. Return Values
  * method1 returned 'Hello, World!'
  * method3 returned None (no return statement)

3. Exceptions
  * method3 threw a RuntimeError with the message string 'Error raised in method3' on line 22

