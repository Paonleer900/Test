import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def example_function():
    time.sleep(1)
    print("Function executed")

if __name__ == "__main__":
    example_function()
