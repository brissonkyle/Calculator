class CalculatorInputError(Exception):
    def __init__(self, message='Invalid Character Input'):
        self.message = message