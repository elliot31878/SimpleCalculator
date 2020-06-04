
class ToolHandler:
    
    def __init__(self, number_1:int, number_2:int):
        super(ToolHandler, self)
        self.number_1: int =  number_1
        self.number_2: int =  number_2

    def execute_app(self):
        print("In Plus Tools")
        return self.number_1 * self.number_2
