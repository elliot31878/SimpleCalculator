"""
create by MR.ROBOT-AG at June(6/4/2020)
this class extend from Observer (child) and add plugin multiplication in program
"""


from interfaces.observer import Observer

from importlib import import_module


class MultiService(Observer):

    def __init__(self):
        super(MultiService, self).__init__()

    def notify(self, message: dict):
        print("[+]Multiplication Observer")
        print("<0>_________________________________<0>")
        number1: int = message.get("number1")
        number2: int = message.get("number2")
        plugin_module_path = r"core.plugins.tool_multi_operator.tools_handler"
        plugin_module = import_module(plugin_module_path)
        plugin = plugin_module.ToolHandler(number1, number2)
        plugin.execute_app()
        print("<0>_________________________________<0>")

    @property
    def class_name(self):
        return "modules.MultiService"