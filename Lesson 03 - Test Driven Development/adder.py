"adder.py: defines an adder function according to a slightly unusual definition"
import numbers

def adder(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return x + [y]
    elif isinstance(y, list) and not isinstance(x, list):
        return y + [x]
    elif isinstance(x, numbers.Number) and isinstance(y, str):
        return str(x) + y
    elif isinstance(y, numbers.Number) and isinstance(x, str):
        return x + str(y)
    elif isinstance(x, str) and isinstance(y, list):
        return [x] + y
    elif isinstance(y, str) and isinstance(x, list):
        return x + [y]
    return x + y