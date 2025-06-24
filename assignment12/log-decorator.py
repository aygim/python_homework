# one time setup
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...
# To write a log record:
logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper(*args,**kwargs):
        print (func.__name__)
        print(args)
        print(kwargs)
        print(func())
        logger.log(logging.INFO, func.__name__)
        logger.log(logging.INFO, args)
        logger.log(logging.INFO, kwargs)
        logger.log(logging.INFO, func())
    return wrapper

@logger_decorator
def print_name():
    print("Hello")

print_name()

@logger_decorator
def myfunction(*args):
    return True

myfunction(1,2,True)


@logger_decorator
def myfunction1(**kwargs):
    return logger_decorator

myfunction1(a=1, b=False)

