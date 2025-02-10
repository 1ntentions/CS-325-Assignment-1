import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        finish = time.time()
        total = finish - start
        print("The function took", total, "seconds to execute")
        return result
    return wrapper

@timer
def main_func():
    time.sleep(1)
    print("Function started")

main_func()