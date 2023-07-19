import time


def exe_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_return = func(*args, **kwargs)
        end = time.time()
        print('{}() execution time: {}s'.format(func.__name__, end - start))
        return func_return

    return wrapper