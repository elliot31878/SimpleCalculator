"""
create by MR.ROBOT-AG at June(6/4/2020)
this class for settingUp  Concentrate
"""


class SettingUpConcentrate:
    
    def __init__(self, param:str, service_path:str, package:object, number1:int, number2:int):
        super(SettingUpConcentrate, self)

        self.param: str = param
        self.service_path: str = service_path
        self.package: object = package
        self.number1: int = number1
        self.number2: int = number2

    def setting_up(self):
        
        """this method for setting up ConcentrateHandler and send notification to child
        """
        from core.concentrate_handlers.concentrate_handler import ConcentrateHandler
        
        concentrate: ConcentrateHandler = ConcentrateHandler()
        concentrate.inject(self.package())
        concentrate.notification(message = {"number1":self.number1, "number2":self.number2} , to = self.service_path)