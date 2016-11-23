def decorator(function):
    def wrapper(*args, **kwargs):
        print 'Start'
        function(*args, **kwargs)
        print 'Finish'
    return wrapper


@decorator
def function():
    print 'Function works'

function()    