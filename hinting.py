from typing import Callable, Tuple, Optional, TypeVar, Any, cast, Dict

# Type hinting
def adder(x: int, y: int) -> None:
    print(f'The total of {x} + {y} = {x+y}')

a: Callable[[int, int], None] = adder

def some_func(x: int, y: Tuple[str, str], z: Optional[float] = None) -> Optional[str]:
    if x > 10:
        return None
    return 'You called some_func'

# Decorators
F = TypeVar('F', bound=Callable[..., Any])

def my_decorator(func: F) -> F:
    def wrapper(*args, **kwds):
        print("Calling", func)
        return func(*args, **kwds)
    return cast(F, wrapper)


# Aliasing
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

# Type Comments
def some_function(a, b, c):
    # type: (str, int, int) -> None
    print(a)
