
def run_code(func, *args, **kwargs):
    func(*args, **kwargs)

def recurring_driver(code_to_execute, interval, callback, *callback_args, **callback_kwargs):
    import time

    while True:
        start_time = time.time()
        code_to_execute()
        elapsed_time = time.time() - start_time
        if elapsed_time < interval:
            time.sleep(interval - elapsed_time)
        else:
            callback(*callback_args, **callback_kwargs)

def my_code_function():
    print("Executing my code function")

def my_callback_function():
    print("Executing my callback function")

# Example usage
recurring_driver(my_code_function, 5, my_callback_function)
