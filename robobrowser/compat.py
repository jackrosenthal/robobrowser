import sys

PY2 = int(sys.version[0]) == 2
PY26 = PY2 and int(sys.version_info[1]) < 7

if PY2:
    unicode = unicode
    basestring = basestring
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    builtin_name = '__builtin__'
else:
    unicode = str
    basestring = (str, bytes)
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    builtin_name = 'builtins'
