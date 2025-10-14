from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызовов функций.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка, выполняющая логирование до и после вызова функции.
            """
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}\n"
                result = None

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message)
            else:
                print(log_message, end="")

            if result is not None:
                return result

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    """
    Простая функция сложения двух чисел.
    """
    return x + y
