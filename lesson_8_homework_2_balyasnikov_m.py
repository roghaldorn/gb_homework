from functools import wraps


def type_logger(show_name=True):
    """
    Decorator: show type of function's return
    """
    def _type_logger(callback):
        @wraps(callback)
        def wrapper(*args):
            wrap_result, def_name = callback(*args), ''
            if show_name:
                def_name = callback.__name__
            result = f'{def_name}({wrap_result}: {type(wrap_result)})'
            # wrapper.__name__, wrapper.__doc__ = callback.__name__, callback.__doc__
            return result
        return wrapper
    return _type_logger


def val_checker(callback_check):
    """
    Decorator: check value in main func by another func(Boolean)
    """
    def _val_checker(callback):
        @wraps(callback)
        def wrapper(*args):
            if callback_check(*args):
                return callback(*args)
            else:
                raise ValueError(f'Wrong value: {args[0]}')
        return wrapper
    return _val_checker


@type_logger(show_name=True)
@val_checker(lambda x: x % 2) # нечетные
def calc_cube(x):
    """
    Calculate x ** 3
    :param x: value, INT
    :return: x ** 3, INT
    """
    return x ** 3


help(calc_cube)
print(calc_cube(11))
