from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args):
        return "<b>" + func(*args) + "</b>"
    return wrapper

@bold
def formatted_text(text):
    """
    Format the passed in text
    """
    return text

print(formatted_text.__name__)
print(formatted_text.__doc__)