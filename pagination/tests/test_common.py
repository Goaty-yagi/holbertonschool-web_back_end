#!/usr/bin/python3
"""
This module is group of test files to that general holberton requirement
of python projects including:
1, first_line_shebang
2, file_is_executable
3, pycode_style
4, all_doc_test
5, mypy

This tests all python file recursively from the base_dir
all the way to the end of the most nested file except files in exceptions.

"""

import unittest
import os
import subprocess

from .base_node_visitor import BaseNodeVisitor

base_dir = './'
exceptions = ['__init__.py', 'tests', 'venv', 'run_files']

class BaseTest(unittest.TestCase):

    def test_commons(self):
        all_filenames = os.listdir(base_dir)
        def recursion(all_file, dir):
            for filename in all_file:
                if filename not in exceptions:
                    if not os.path.isdir(dir + filename):
                        if filename.endswith('.py'):
                            print("filename", filename)
                            full_path = os.path.join(dir, filename)
                            self.first_line_shebang_test(full_path)
                            self.file_is_executable_test(full_path)
                            self.pycode_style_test(full_path)
                            self.all_doc_test(full_path)
                            self.mypy_test(full_path)
                    else:
                        all_filenames = os.listdir(dir + filename)
                        new_dir = dir + filename + '/'
                        recursion(all_filenames, new_dir)
        recursion(all_filenames, base_dir)

    def first_line_shebang_test(self, path):
        """ Testing the first line of a specific file is expected. """
        shebang = "#!/usr/bin/env python3\n"

        with open(path, 'r') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print(f"Error: Your file {path} has no content.")

        self.assertEqual(lines[0], shebang, f"{path} has no shebang {shebang}")

    def file_is_executable_test(self, path: str):
        """ Testing the target file is executable. """

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable, f"{path} should be executable")

    def pycode_style_test(self, path: str):
        """ Testing  a specific file meet pep8 requirements """

        command = ["pycodestyle", path]
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Check if pycodestyle result is successful (exit code 0)
        self.assertEqual(result.returncode, 0,
                         f"pycodestyle check failed:\n{result.stdout}")

    def all_doc_test(self, path: str) -> None:
        """ Testing  module, classes and functions in the module
        are all documented.
        """
        with open(path, 'r') as file:
            read_content = file.read()
        visitor = BaseNodeVisitor(read_content)
        for doc_dict in visitor.doc_list:
            self.assertTrue(
                doc_dict["doc"], f"Your {doc_dict['name']} has no documentation.")

    def mypy_test(self, path: str):
        """ Testing  a specific file meet pep8 requirements """

        command = ["mypy", path]
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Check if pycodestyle result is successful (exit code 0)
        self.assertEqual(result.returncode, 0,
                         f"mypy check failed:\n{result.stdout}")
