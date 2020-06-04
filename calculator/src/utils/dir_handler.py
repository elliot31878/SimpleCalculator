"""
    - created by muhammad shabestari at April 23/2020
    - this app created for managing directories with python
"""

import os


class DirManager:
    """ directory manager """

    def __init__(self):
        super(DirManager, self).__init__()

        self.current_directory = os.getcwd()

    @property
    def current_dir(self):
        """ this method return current directory that application run from it
            :return: current directory as string
        """
        return self.current_directory

    def get_all_directory(self, path, level: int = 0):

        """ get all directory that exist in path
            :param path: directory path
            :param level: depth of crawling
            :return: list of directories
        """
        main_dir = path.rstrip(os.path.sep)
        assert os.path.isdir(main_dir)

        main_dir_level = main_dir.count(os.path.sep)
        for root, dirs, _ in os.walk(main_dir):
            list_dirs = [item for item in dirs if not item == "__pycache__"]
            num_sep_this = root.count(os.path.sep)
            if main_dir_level + level <= num_sep_this:
                del dirs[:]
        list_dirs.sort(reverse=True)

        return list_dirs
