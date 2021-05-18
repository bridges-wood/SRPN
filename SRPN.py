import re

from handlers import (handle_d, handle_equals, handle_number, handle_operator,
                      handle_r)
from one_liner import dense_split, reorder
from operations import is_double_operator, is_number, is_operator

stack = []
comment_mode = False
# Max length can be 23.


def main():
    """The main function that runs all the logic for the application.
    """
    print("You can now start interacting with the SRPN calculator")
    while True:
        commands = format_input(input())
        execute_commands(commands)


def format_input(input: str):
    """Reformats input so that it can be comprehended.

    Args:
        input (str): Raw command line input.

    Returns:
        (list): A list of all the commands that need to be executed.
    """
    return to_command_array(input)


def to_command_array(cleaned_input: str):
    """Takes a string and turns it into an array of operations.

    Args:
        cleaned_input (str): The command line input without comments.

    Returns:
        (list): A list of commands.
    """
    if ' ' in cleaned_input:
        return re.split(' ', cleaned_input)
    else:
        try:
            # Attempts to evaluate any inline arithmetic
            working_input = cleaned_input.replace('^', '**')
            evaluation = str(eval(working_input))
            return [evaluation]
        except:
            split_commands = dense_split(cleaned_input)
            return reorder(split_commands)


def execute_commands(commands: list):
    """Executes each command in the list.

    Args:
        commands (list): The list of commands to be executed.
    """
    global stack
    global comment_mode
    for command in commands:
        if comment_mode and command != '#':
            continue
        try:
            if is_number(command):
                stack = handle_number(command, stack)
            elif is_operator(command):
                stack = handle_operator(command, stack)
            elif is_double_operator(command):
                handle_equals(stack)
                stack = handle_operator(command[0], stack)
            elif command == '=':
                handle_equals(stack)
            elif command == 'd':
                handle_d(stack)
            elif command == 'r':
                stack = handle_r(stack)
            elif command == '#':
                comment_mode = not comment_mode
            else:
                print("Unrecognised operator or operand \"" + command + "\"")
        except OverflowError:
            print("Stack overflow.")


if __name__ == "__main__":
    main()
