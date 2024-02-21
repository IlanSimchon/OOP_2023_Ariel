import time


# Decorator function to measure the execution time of a function
def measure_time(func):
    def wrapper(*args, **kwargs):
        print("Starting stopper")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time} seconds to execute.")
        return result

    return wrapper


# Decorator function to log the arguments and return value of a function
def log_arguments_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


# Example function with both decorators applied
@measure_time
@log_arguments_and_return
def complex_calculation(x, y):
    # Simulate a complex calculation
    i = 0
    while i < 5:
        time.sleep(0.6)
        print("Very difficult calculations....")
        i += 1
    return x * y


# Using the decorated function
result = complex_calculation(3, 4)
