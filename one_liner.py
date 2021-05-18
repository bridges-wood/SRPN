def create_types_dict():
    """Generates a dictionary of types for each valid command that might be encountered.

    Returns:
        (dict): A dictionary of command types.
    """
    types = dict.fromkeys(['+', '-', '/', '*', '%', '^', '='], 'operator')
    types.update(dict.fromkeys(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 'digit'))
    types.update({'d': 'display'})
    types.update({'r': 'random'})
    return types


TYPES = create_types_dict()


def dense_split(cleaned_input: str):
    """Converts a str of dense commands into an array that can be executed b

    Args:
        cleaned_input (str): The command line input with all comments removed.

    Returns:
        (list): List of commands extracted from the string.
    """
    char_array = [char for char in cleaned_input]
    return combine_commands(char_array)


def combine_commands(current_array: list):
    """Recursively combines adjacent commands in the command array.

    Args:
        current_array (list): The current array of the commands.

    Returns:
        (list): The correctly combined command list.
    """
    next_array = [current_array[0]]
    change_made = False
    for index in range(1, len(current_array)):
        combination = combine_adjacent(next_array[-1], current_array[index])
        if isinstance(combination, str):
            next_array[-1] = combination
            change_made = True
        else:
            next_array.append(current_array[index])

    if not change_made:
        return next_array
    else:
        return combine_commands(next_array)


def combine_adjacent(a: str, b: str):
    """Combines two strings if their respective types (as described by type_of) are the same.

    Args:
        a (str): The first string to be checked.
        b (str): The second string to be checked.

    Returns:
        Either the two strings concatenated or an array containing both.
    """
    if type_of(a) == type_of(b) and type_of(a) != 'random' and type_of(a) != 'display' and type_of(a) != 'unknown':
        return a + b
    else:
        return [a, b]


def type_of(target: str):
    """Determines the type of a string using a dictionary of types.

    Args:
        target (str): [description]

    Returns:
        [type]: [description]
    """
    try:
        return TYPES[target[0]]
    except KeyError:
        return 'unknown'


def reorder(commands: list):
    """To be more like the original SRPN, some terms in the command array must be reordered.

    Args:
        commands (list): The list of commands to be reordered.

    Returns:
        (list): The correctly ordered list of commands.
    """
    for index in range(0, len(commands) - 1):
        # If there's an operator followed by a number, swap them.
        if type_of(
                commands[index]) == 'operator' and type_of(
                commands[index + 1]) == (
                'digit' or 'random'):
            commands[index], commands[index + 1] = commands[index + 1], commands[index]
    result = []
    for index in range(0, len(commands)):
        if len(commands[index]) == 2 and '=' in commands[index]:
            result.insert(-1, '=')
            result.append(commands[index][0])
        else:
            result.insert(0, commands[index])
    return result
