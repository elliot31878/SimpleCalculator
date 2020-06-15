"""
    create by MR.ROBOT-AG at June(6/5/2020)
    - this class base us application for initializer or settingUp application
"""


class StartUp:

    def __init__(self):
        super(StartUp, self)

    @staticmethod
    def __start_services__():
        from modules.services.tool_manager.tool_manager import ToolManager

        ToolManager()

        from modules.services.consoleapp.presentation import Presentation

        p = Presentation()
        p.show_elements()

    def start_app(self):
        self.__start_services__()