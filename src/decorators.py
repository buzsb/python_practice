import time


def start_and_finish_decorator(func):
    def wrapper(*args, **kwargs):
        print 'Start'
        result = func(*args, **kwargs)
        print 'Finished with result {result}'.format(result=result)
        return result
    return wrapper


@start_and_finish_decorator
def function():
    text = 'Function works'
    print text
    return text
    

def run_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print 'Function runs {run_time} seconds'.format(run_time=run_time)
        return run_time
    return wrapper


@run_time_decorator
def list_doubler(array):
    result = [i * 2 for i in array]
    print result
    return result


if __name__ == '__main__':
    function() 
    list_doubler([2, 3, 4])
