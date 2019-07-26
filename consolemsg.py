#!/usr/bin/env python
# -*- encoding: utf8 -*-

def _decoratedStream(stream):
    # respect the encoding if set
    if stream.encoding:
        return stream
    # if not use utf8
    import codecs
    return codecs.getwriter('utf8')(stream)

def stderr():
    if hasattr(stderr, 'cached'):
        return stderr.cached
    import sys
    stderr.cached = _decoratedStream(sys.stderr)
    return stderr.cached

def stdout():
    if hasattr(stdout, 'cached'):
        return stdout.cached
    import sys
    stdout.cached = _decoratedStream(sys.stdout)
    return stdout.cached

def b(text):
    if type(text) == type(b''): return text
    if type(text) == type(u''): return text.encode('utf8')
    return type(u'')(text).encode('utf8')

def u(text):
    if type(text) == type(u''): return text
    if type(text) == type(b''): return text.decode('utf8')
    return type(u'')(text)

def printStdError(*args) :
    stderr().write(u' '.join(u(arg) for arg in args))
    stderr().write(u'\n')
    stderr().flush()

def printStdOut(*args) :
    stdout().write(u' '.join(u(arg) for arg in args))
    stdout().write(u'\n')
    stdout().flush()

def color(color, message, *args, **kwds):
    if args or kwds:
        message=u(message).format(*args,**kwds)
    return u"\033[{0}m{1}\033[0m".format(u(color),u(message))

def success(message, *args, **kwds):
    printStdError(color('32;1', ">> "+u(message), *args, **kwds))

def step(message, *args, **kwds):
    printStdError(color('34;1', ":: "+u(message), *args, **kwds))

def error(message, *args, **kwds):
    printStdError(color('31;1', "Error: "+u(message), *args, **kwds))

def warn(message, *args, **kwds):
    printStdError(color('33', "Warning: "+u(message), *args, **kwds))

def fail(message, code=-1, *args, **kwds):
    error(message, *args, **kwds)
    import sys
    sys.exit(code)

def out(message, *args, **kwds):
    printStdOut(u(message).format(*args,**kwds))


if __name__ == "__main__":
    step('Testing common messages')
    success('Success!')
    warn('This might be dangerous')
    error('Something bad happened')
    step('Testing common messages')
    success('{} did this', 'Joe')
    warn('{thing} might be dangerous', thing="Swords")
    # Parameters
    error(u'Unicode castaña unicode param {what}', what=u"castañin") # Beyond ASCIII use unicode
    error(b'Encoded casta\xc3\xb1a unicode param {what}', what=u"castañin") # Some permisivity with templates, not with params
    error('{what} happened', what="Murphy")
    error(2323) # Message is converted to unicode
    out('This goes {} to the output', 'undecorated')
    out(u'Supporting castañas as well')
    out(b'Supporting encoded casta\xc3\xb1as as well')
    fail('Something very bad happened and i will die. {}', -2, 'Bye')



# vim: et ts=4 sw=4
