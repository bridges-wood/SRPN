from copy import deepcopy


def is_operator(command: chr):
    """Checks if a given command is an operator.

    Args:
        command (chr): The command to be checked.

    Returns:
        (bool): Whether or not the command is an operator.
    """
    operators = ('+', '-', '/', '*', '%', '^')
    return command in operators


def is_double_operator(command: str):
    """Checks whether or not a command is of the form "(operator)=".

    Args:
        command (str): THe command to be checked.

    Returns:
        (bool): Whether or not the command is a double operator.
    """
    operators = ("+=", "-=", "/=", "*=", "%=", "^=")
    return command in operators


def is_number(command: str):
    """Checks if a given command is an integer.

    Args:
        command (str): The command to be checked.

    Returns:
        (bool): Whether or not the command is an int.
    """
    try:
        int(command)
        return True
    except ValueError:
        return False


def execute_operation(operator: str, stack: list):
    """Executes the operation described by an appropriate operator.

    Args:
        operator (str): The operator to be executed.
        stack (list): The current state of the stack.

    Raises:
        ZeroDivisionError

    Returns:
        (list): The new state of the stack.
    """
    # A working copy of the stack has to be created in order to avoid any problems with invalid operations changing the stack.
    working_stack = deepcopy(stack)
    try:
        b = working_stack.pop()
        a = working_stack.pop()
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if a == 0:
                raise ZeroDivisionError
            result = a // b
        elif operator == '%':
            result = a % b
        elif operator == '^':
            result = a ** b

        if result > 2147483647:
            working_stack.append(2147483647)
        elif result < -2147483648:
            working_stack.append(-2147483648)
        else:
            working_stack.append(result)
    except IndexError:
        print("Stack underflow.")
        return stack
    except ZeroDivisionError:
        print("Divide by 0.")
        return stack
    else:
        return working_stack


def describe(stack: list):
    """Prints the value of each element in the stack to the command line.

    Args:
        stack (list): The current state of the stack.
    """
    for number in stack:
        print(number, end='\n')
