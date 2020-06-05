"""
create by MR.ROBOT-AG at June(6/4/2020)
this class for handle observer services
"""


class ObserverServicesHandler:
    def __init__(self):
        super(ObserverServicesHandler, self)
        self.number_1: int = 0
        self.number_2: int = 0
        self.param: str = ""

    def __setting_up_calculate_ui__(self):

        """this method for initializer settingUp CalculateUi

        Returns:
            [int , int , str] -- [number one , number two send with param example param is + , - or //]
        """

        try:

            number_1: int = int(input("Enter number one : "))
            number_2: int = int(input("Enter number two : "))

            param: str = str(input("Enter param: "))

            if not (len(param) == 1 and (param.__contains__("+")) or (
                    param.__contains__("-") or param.__contains__("*") or (param.__contains__("/")))):
                # your params is wrong
                print("Your Param its Wrong")
                return None
            # SuccessFully
            return number_1, number_2, param

        except Exception:
            print(TypeError("your input has wrong type"))
            return None

    def observer_handler(self):

        """this method for initializer calculate ui and  get number and get self.param and return self.param service path and Service Class

        Returns:
            [arg1 = string, arg2 = string, arg3 = object, args4 = int ]: [one argument return params tow argument return  service path ,
            argument three return need object  for calculate & argument four return result(sum, minus, multiplication, devision)]
        """
        print("<>-----------------------------------<>")
        try:
            self.number_1, self.number_2, self.param = self.__setting_up_calculate_ui__()
        except:
            self.observer_handler()
        print("<>------------------------------------<>")

        # switch in self.param
        # +
        if self.param == "+":

            from modules.Services.plus_service import PlusService
            return self.param, "modules.PlusService", PlusService, self.number_1, self.number_2
        # -
        elif self.param == "-":

            from modules.Services.minus_service import MinusService
            return self.param, "modules.MinusService", MinusService, self.number_1, self.number_2
        # *
        elif self.param == "*":

            from modules.Services.multiplication_service import MultiService
            return self.param, "modules.MultiService", MultiService, self.number_1, self.number_2
        # /
        elif self.param == "/":

            from modules.Services.div_service import DivisinService
            return self.param, "modules.DivisionService", DivisinService, self.number_1, self.number_2
