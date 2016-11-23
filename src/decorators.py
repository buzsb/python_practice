def start_and_finish_decorator(func):
    def wrapper(*args, **kwargs):
        print 'Start'
        result = function(*args, **kwargs)
        print 'Finished with result {result}'.format(result=result)
        return result
    return wrapper


@start_and_finish_decorator
def function():
    text = 'Function works'
    print text
    return text


if __name__ == '__main__':
    function()    