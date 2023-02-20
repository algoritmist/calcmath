from functools import reduce


def interactive_mode():
    pass


def file_mode():
    pass


def random_mode():
    pass


keys = [
    ("-i", "interactive mode", interactive_mode),
    ("-f", "file mode", file_mode),
    ("-r", "random generation mode (for testing)", random_mode)
]

def to_str(key):
    return key[0] + ' - ' + key[1]
def keys_to_str():
    return reduce(lambda x, y: x + to_str(y) + '\n', keys, "")


def get_info():
    program_info = "MatrixSolver - the program that solves LES with the method of simple iterations"
    keys_info = "You can use the following keys to run the program:\n" + keys_to_str()
    return program_info + '\n' + keys_info