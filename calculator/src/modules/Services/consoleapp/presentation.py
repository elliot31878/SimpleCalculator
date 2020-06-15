from ..tool_manager.tool_manager import ConcentrateHandler


class Presentation:

    def __init__(self):
        super(Presentation, self).__init__()

        self.con_handler = ConcentrateHandler()

    def show_elements(self):
        number_1: int = int(input("Enter number 1: "))
        number_2: int = int(input("Enter number 2: "))

        operator: str = input("Enter operator(+, -, /, *): ")

        if operator != "+" or operator != "-" or operator != "/" or operator != "*":
            assert Exception, f"This operator {operator} not support in program"

        print(self.con_handler.notification(message={
            "number1": number_1,
            "number2": number_2
        }, to=f"{operator}"))