import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        post_time = time.time()
        print(f"Time taken to run {function.__name__} : {post_time - start_time}s")

    # return wrapper_function() # If it not called here it can be called during main function call
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
