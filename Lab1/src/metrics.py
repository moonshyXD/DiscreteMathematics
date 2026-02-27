from time import time
from functools import wraps
from typing import Callable, Any


def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time()

        result = func(*args, **kwargs)

        end_time = time()
        elapsed = end_time - start_time
        print(f"The task '{func.__name__}' took {elapsed:.8f} seconds to complete.")

        return result

    return wrapper
