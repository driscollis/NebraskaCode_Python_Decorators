import functools
import logging

def exceptionLogger(func, loggerName=''):
    """
    A simple decorator that will catch and log any exceptions that may occur
    to the root logger.
    """
    assert callable(func)
    mylogger = logging.getLogger(loggerName)

    # wrap a new function around the callable
    def logger_func(*args, **kw):
        try:
            if not kw:
                return func(*args)
            return func(*args, **kw)
        except Exception:
            mylogger.exception('Exception in %s:', func.__name__)

    logger_func.__name__ = func.__name__
    logger_func.__doc__ = func.__doc__
    if hasattr(func, '__dict__'):
        logger_func.__dict__.update(func.__dict__)
    return logger_func


def exceptionLog2Logger(loggerName):
    """
    A decorator that will catch and log any exceptions that may occur
    to the named logger.
    """
    import functools
    return functools.partial(exceptionLogger, loggerName=loggerName)

@exceptionLog2Logger('test_except_logger')
def test_exception():
    1 / 0

if __name__ == '__main__':
    """
    See https://www.blog.pythonlibrary.org/2014/03/14/wxpython-catching-exceptions-from-anywhere/
    for more information
    """
    test_exception()