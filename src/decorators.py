def decorator(function):
    def wrapper(*args, **kwargs):
        print 'Start'
        result = function(*args, **kwargs)
        print 'Finish {result}'.format(result=result)
    return wrapper


@decorator
def function():
    text = 'Function works'
    print text
    return text


if __name__ == '__main__':
    function()    