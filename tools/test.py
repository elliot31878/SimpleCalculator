"""
create by MR.ROBOT-AG at June(6/5/2020)
----this package test Application File
"""

if __name__ == '__main__':
    from tool_div_operator.tools_handler import ToolHandler

    ToolHandler(10, 2).execute_app()

    from tool_multi_operator.tools_handler import ToolHandler

    ToolHandler(10, 2).execute_app()

    from tool_minus_operator.tools_handler import ToolHandler

    ToolHandler(10, 2).execute_app()

    from tool_plus_operator.tools_handler import ToolHandler

    ToolHandler(10, 2).execute_app()

# test is SuccessFully
