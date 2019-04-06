import re


class GetInpuValuesService(object):
    """ GetInputValuesService parses the input string provided and returns it's values

    Attributes:
        input_line(str): input that contains the necessary values to perform a checkout.
                         The input line is expected to be: A, B, 3C, A
    Returns:
        List containing all the input values. If the input is invalid returns an empty list.
    """
    def __init__(self, input_line):
        self.input_line = input_line

    def call(self):
        split_input_values_regex = re.compile('[0-9]*[A-Z]')
        return split_input_values_regex.findall(self.input_line)
