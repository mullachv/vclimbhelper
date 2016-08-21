import sys
import collections

#
# Call this class in the following sequence:
#
# tracer = Tracer()
# tracer.set_trace_methods(['method1', 'method2'])
# tracer.start()
#
# Now, call the target method(s) of interest
#
# Then call one or more of these:
#   get_calllist_iterator
#   get_returnlist_iterator
#   get_exceptionlist_iterator
#
# Optionally print using tracer.printStats()
# Finally, reset by tracer.reset() before calling the next set of methods
#
#
class Tracer(object):
    def __init__(self):
        self._attr_call_list = []
        self._attr_trace_into = []
        self._attr_return_list = []
        self._attr_exceptions_list = []

    def set_trace_methods(self, alist):
        self._attr_trace_into = alist

    def printStats(self):
        print "### Called Methods ###"
        for item in self._attr_call_list:
            print item
        print "### Method Return Values ###"
        for item in self._attr_return_list:
            print item
        print "### Method Exceptions ###"
        for item in self._attr_exceptions_list:
            print item
        return

    def start(self):
        sys.settrace(self.__trace_calls_and_returns)

    def get_returnlist_iterator(self):
        return iter(self._attr_return_list)

    def get_calllist_iterator(self):
        return iter(self._attr_call_list)

    def get_exceptionlist_iterator(self):
        return iter(self._attr_exceptions_list)

    def reset(self):
        sys.settrace(None)
        del self._attr_call_list[:]
        del self._attr_return_list[:]
        del self._attr_exceptions_list[:]
        del self._attr_trace_into[:]

    def __trace_calls_and_returns(self, frame, event, arg):
        '''
        This method does three things:
        - Captures called method info (for method calls)
        - Captures function name and return value for method returns
        - Captures exception details if the event is an exception and this is
            a method of interest to us
        Reference: https://pymotw.com/2/sys/tracing.html
        '''

        co = frame.f_code
        func_name = co.co_name
        if func_name == 'write' or func_name == 'printStats':
            return
        func_line_no = frame.f_lineno
        func_filename = co.co_filename
        if event == 'call':
            item = {}
            item['func_name'] = func_name
            item['func_line_no'] = func_line_no
            item['func_filename'] = func_filename
            self._attr_call_list.append(item)
            return self.__trace_calls_and_returns
        elif event == 'return':
            item = {}
            item['func_name'] = func_name
            item['return_value'] = arg
            self._attr_return_list.append(item)
        elif event == 'exception':
            if func_name in self._attr_trace_into:
                exc_type, exc_value, exc_traceback = arg
                item = {}
                item['exception_name'] = exc_type.__name__
                item['exception_value'] = exc_value
                item['func_name'] = func_name
                item['func_line_no'] = func_line_no
                self._attr_exceptions_list.append(item)
        return
