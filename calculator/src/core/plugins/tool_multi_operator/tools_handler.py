"""
create by MR.ROBOT-AG at June(6/5/2020)
this class for multiplication between two number
"""


from .interfaces.observer import Observer


class ToolHandler(Observer):
    
    def __init__(self):
        super(ToolHandler, self)

    @property
    def class_name(self):
        return "*"

    def execute_app(self, message):
        number_1: int = message["number1"]
        number_2: int = message["number2"]

        return number_1 * number_2
