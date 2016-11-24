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
    
def run_time_decorator(func_run_times = 1):
    def run_time_functions(func):
        def wrapper(*args, **kwargs):
            summary_run_time = 0
            for i in range(func_run_times):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                summary_run_time += end_time - start_time

            average_run_time = summary_run_time / func_run_times
            print (
                'Average {runs} functions performed '
                'by {time} seconds each'
                .format(runs=func_run_times, time=average_run_time)
            )
            return average_run_time
        return wrapper
    return run_time_functions


@run_time_decorator(3)
def list_doubler(array):
    result = [i * 2 for i in array]

    return result


if __name__ == '__main__':
    function() 
    list_doubler([2, 3, 4])
