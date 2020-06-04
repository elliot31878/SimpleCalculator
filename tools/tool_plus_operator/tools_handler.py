"""
create by MR.ROBOT-AG at June(6/5/2020)
this class for plus between two number
"""


class ToolHandler:
    
    def __init__(self, number_1:int, number_2:int):
        super(ToolHandler, self)
        self.number_1: int =  number_1
        self.number_2: int =  number_2

    def execute_app(self):
        print("In Plus Tools")
        print(self.number_1 + self.number_2)
        return  self.number_1 + self.number_2
