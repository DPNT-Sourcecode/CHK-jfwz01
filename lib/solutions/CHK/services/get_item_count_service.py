import re


class GetItemCountService(object):
    """ GetInputValuesService parses the input string provided and returns a dict containing the count of each item.

    Attributes:
        input_line(str): input that contains the necessary values to perform a checkout.
                         The input line is expected to be: AAAABBBCCCCCCCAAA
    Returns:
        <Dict> containing the count of each item.
    """
    def __init__(self, input_line):
        self.input_line = input_line

    def call(self):
        input_values_regex = re.compile('[A-Z]')
        input_values = input_values_regex.findall(self.input_line)

        inputs_values_count = {}
        for input_value in input_values:
            if input_value in inputs_values_count:
                inputs_values_count[input_value] += 1
            else:
                inputs_values_count[input_value] = 1
        return inputs_values_count
