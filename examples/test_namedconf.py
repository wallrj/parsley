from namedconf import NamedConfParser as NCP
import unittest

class NamedConfParserTests(unittest.TestCase):

    def test_directiveWithoutValue(self):
        """
        A directive without a value returns a None value.
        """
        self.assertEqual(
            NCP("mydirective;").directive(), ('mydirective', None))
