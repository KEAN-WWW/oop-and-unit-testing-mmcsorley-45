from app.addition import add
from app.subtraction import subtract
from app.multiplication import multiply
from app.division import divide


class Calculator(object):
    @staticmethod
    def addition(val1,val2):
        return add(val1,val2)

    @staticmethod
    def subtraction(val1,val2):
        return subtract(val1,val2)

    @staticmethod
    def multiplication(val1,val2):
        return multiply(val1,val2)

    @staticmethod
    def division(val1,val2):
        return divide(val1,val2)
