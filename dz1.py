import time
from functools import wraps


def time_my_function(f):
    @wraps(f)
    def answer_f(*args, **kwargs):
        t0 = time.monotonic()
        return_value = f(*args, **kwargs)
        print(f'Function {f.__name__} took {time.monotonic() - t0} seconds to complete')
        return return_value

    return answer_f


@time_my_function
def say_hello():
    print('Hello')



say_hello()

print(say_hello)

def say_hello():
    print('Hello')
print(say_hello)