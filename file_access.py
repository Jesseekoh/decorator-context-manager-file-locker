"""This module implements a FileAccess context manager class for file handling.
"""
import os


class FileAccess:
    def __init__(self, filepath, mode='r'):
        """Initialize FileAccess object for managing file operations.

        Args:
            filename (str): filepath
            mode (str, optional): Mode to open file in. Defaults to 'r'.
        """
        self.filepath = filepath
        self.__mode = mode
        self.file = None
        self.filesize = 0

    def __enter__(self):
        """Opens the file and returns the file object.

        This method is used to set up the context when using the 'with' statement

        Returns:
            IO: The opened file object
        """
        self.file = open(self.filepath, mode=self.__mode, encoding='utf8')
        self.filesize = os.path.getsize(self.filepath)
        return self.file

    def __exit__(self, type, value, traceback):
        """Closes the file object and handles any exception"""
        self.file.close()
