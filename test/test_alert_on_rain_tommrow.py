from unittest import TestCase, mock
from alert_on_rain.alert_on_rain_tomorrow_runner import *

import os


class BaseTests(TestCase):

    def test_command_line_args_empty(self):
        reply = "some_kind_of_test_here"
        self.assertIsNone(reply)
