import time


def start_and_finish_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@start_and_finish_decorator
def function():
    text = 'Function works'
    return text


def run_time_decorator(func_run_times=1):
    def run_time_functions(func):
        def wrapper(*args, **kwargs):
            summary_run_time = 0
            for i in range(func_run_times):
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                summary_run_time += end_time - start_time

            average_run_time = summary_run_time / func_run_times
            return average_run_time
        return wrapper
    return run_time_functions


@run_time_decorator(3)
def list_doubler(array):
    result = [i * 2 for i in array]

    return result


if __name__ == '__main__':
    print function()
    print list_doubler([2, 3, 4])
