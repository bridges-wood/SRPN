from operations import describe, execute_operation
from random_numbers import get_next_random_number


def handle_number(symbol: str, stack: list):
    """Deals with all number inputs.

    Args:
        symbol (str): The number inputted by the user to be pushed to the stack.
        stack (list): The stack for the number to be pushed to.

    Raises:
        OverflowError: Raised if pushing the number would increase the length of the stack to more than 23.

    Returns:
        list: The stack with the number pushed to it, if it is a valid operation.
    """
    if stack_overflow(stack):
        raise OverflowError
    else:
        to_append = parse_number(symbol)
        stack.append(to_append)
    return stack


def stack_overflow(stack: list):
    """Checks if the stack is currently full.

    Args:
        stack (list): The stack.

    Returns:
        (bool): Whether or not the stack is full.
    """
    return len(stack) == 23


def parse_number(number: str):
    """Parses any numbers to be added to the stack.

    Args:
        number (str): The number to be added to the stack.

    Returns:
        (int): The integer representation of the string input.
    """
    if number.startswith('0'):
        return int(number, base=8)  # Handles octal numbers.
    else:
        return int(number)


def handle_operator(symbol, stack: list):
    """Handles the execution of operations on the contents of the stack.

    Args:
        symbol (chr): The mathematical operation to be executed.
        stack (list): The current stack.

    Returns:
        (list): The stack after the operation has been applied.
    """
    return execute_operation(symbol, stack)


def handle_equals(stack: list):
    """Prints the top item in the stack.

    Args:
        stack (list): The current stack.
    """
    print(stack[-1]) if len(stack) != 0 else print("Stack empty.")


def handle_d(stack: list):
    """Handles the description of the stack.

    Args:
        stack (list): The current state of the stack.
    """
    describe(stack) if len(stack) > 0 else print(-2147483648)


def handle_r(stack: list):
    """Handles the addition of 'random' numbers to the stack.

    Args:
        stack (list): The current stack.

    Raises:
        OverflowError: Raised if pushing the random number to the stack would overflow it.

    Returns:
        (list): The stack with the random number pushed to it.
    """
    if stack_overflow(stack):
        raise OverflowError
    else:
        stack.append(get_next_random_number())
    return stack
