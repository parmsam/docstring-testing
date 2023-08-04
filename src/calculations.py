def add(a,b):
    '''This function adds two numbers together

    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Sum of a and b

    Examples:
        >>> add(1,2)
        3.0
        >>> add(1.5,2.5)
        4.0
    '''
    return float(a+b)

def subtract(a,b):
    '''This function subtracts two numbers together
    
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Difference of a and b

    Examples:
        >>> subtract(1,2)
        -1.0
        >>> subtract(1.5,2.5)
        -1.0
    '''
    return float(a-b)

def multiply(a,b):
    '''This function multiplies two numbers

    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Product of a and b

    Examples:
        >>> multiply(1,2)
        2.0
        >>> multiply(1.5,2.5)
        3.75
    '''
    return float(a*b)

def divide(a,b):
    '''This function divides two numbers

    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Quotient of a and b
    Raises:
        ZeroDivisionError: If b is zero

    Examples:
        >>> divide(1,2)
        0.5
        >>> divide(1.5,2.5)
        0.6
    '''
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return float(a/b)
