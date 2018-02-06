#!/usr/bin/env python3

def printStdError(*args) :
    import sys
    sys.stderr.write(' '.join(str(arg) for arg in args))
    sys.stderr.write('\n')
    sys.stderr.flush()

def color(color, message, *args, **kwds) :
    if args or kwds:
        message=message.format(*args,**kwds)
    return "\033[{0}m{1}\033[0m".format(color,message)

def success(message, *args, **kwds) :
    printStdError(color('32;1', ">> "+message, *args, **kwds))

def step(message, *args, **kwds) :
    printStdError(color('34;1', ":: "+message, *args, **kwds))

def error(message, *args, **kwds) :
    printStdError(color('31;1', "Error: "+message, *args, **kwds))

def warn(message, *args, **kwds) :
    printStdError(color('33', "Warning: "+message, *args, **kwds))

def fail(message, code=-1, *args, **kwds) :
    error(message, *args, **kwds)
    import sys
    sys.exit(code)


if __name__ == "__main__":
    step('Testing common messages')
    success('Success!')
    warn('This might be dangerous')
    error('Something bad happened')
    step('Testing common messages')
    success('{} did this', 'Joe')
    warn('{thing} might be dangerous', thing="Swords")
    error('{what} happened', what="Murphy")
    fail('Something very bad happened and i will die. {}', -2, 'Bye')


