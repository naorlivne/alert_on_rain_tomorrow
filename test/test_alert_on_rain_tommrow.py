from unittest import TestCase, mock
import os


class BaseTests(TestCase):

    def test_command_line_args_empty(self):
        reply = "some_kind_of_test_here"
        self.assertIsNone(reply)
