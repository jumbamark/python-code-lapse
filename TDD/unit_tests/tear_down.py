import unittest


class WidgetTestCase(unittest.TestCase):
    def SetUp(self):
        self.Widget = Widget('The Widget')

    def tearDown(self):
        self.Widget.dispose()
