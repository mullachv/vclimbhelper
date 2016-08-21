from nose.tools import *

import sys
import calltrace

def setup():
    pass

def teardown():
    pass

def test_basic():
    pass

def method1():
    return 'Hello, World!'

def method2():
    pass

def method3():
    raise RuntimeError('Error raised in method3')

'''
Run using nosetests -s / --nocapture
Test method with no return
'''
def test_basic1():
    from calltrace import Tracer
    tracer = Tracer()
    tracer.set_trace_methods(['method1'])
    tracer.start()

    method1()

    for item in tracer.get_returnlist_iterator():
        if item['func_name'] == 'method1':
            assert_equal('Hello, World!', item['return_value'])
            break

    tracer.printStats()
    tracer.reset()
    print ""

'''
Run using nosetests -s / --nocapture
Verify method callers
'''
def test_basic2():
    from calltrace import Tracer
    tracer = Tracer()
    tracer.start()

    method2()

    for item in tracer.get_calllist_iterator():
        if item['func_name'] == 'method2':
            assert_equal(18, item['func_line_no'])
            break

    tracer.printStats()
    tracer.reset()
    print ""

'''
Run using nosetests -s / --nocapture
Test method3 that raises exceptions
'''
def test_basic3():
    from calltrace import Tracer
    tracer = Tracer()
    tracer.set_trace_methods(['method3'])
    tracer.start()

    try:
        method3()
    except Exception, e:
        pass

    #item = tracer.get_returnlist_iterator().next()
    #assert_equal('method3', item['func_name'])
    tracer.printStats()
    tracer.reset()
    print ""

'''
Run using nosetests -s / --nocapture
Tests method1 and method3 one after the other - method1 returns a value, method3
raises exception
'''
def test_basic4():
    from calltrace import Tracer
    tracer = Tracer()
    tracer.set_trace_methods(['method3', 'method1'])
    tracer.start()

    try:
        method1()
        method3()
    except Exception, e:
        pass

    #item = tracer.get_returnlist_iterator().next()
    #assert_equal('method3', item['func_name'])
    tracer.printStats()
    tracer.reset()
    print ""
