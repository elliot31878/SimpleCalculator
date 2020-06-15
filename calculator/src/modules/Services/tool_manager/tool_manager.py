
from utils.dir_handler import DirManager
from core.concentrate_handlers.concentrate_handler import ConcentrateHandler

from importlib import import_module


class ToolManager:
    
    def __init__(self):
        super(ToolManager, self).__init__()

        self.dir_manager = DirManager()
        self.concentrate_handler = ConcentrateHandler()

        self.__init_tools__()

    def __init_tools__(self):

        tools_list_name = [
            tool for tool in self.dir_manager.get_all_directory(
                f"{self.dir_manager.current_dir}/core/plugins/"
            )
        ]

        for tool_name in tools_list_name:
            plugin_module_path = f"core.plugins.{tool_name}.tools_handler"
            plugin_module = import_module(plugin_module_path)
            plugin = plugin_module.ToolHandler()
            self.concentrate_handler.inject(plugin)
