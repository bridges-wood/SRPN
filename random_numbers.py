random_numbers = [
    1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492,
    596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926,
    1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]
next_random_number = 0


def get_next_random_number():
    """Fetches the next random number from the set used by SRPN.

    Returns:
        (int): The next "random" number.
    """
    global next_random_number
    random_number = random_numbers[next_random_number]
    next_random_number = (next_random_number + 1) % 22
    return random_number
