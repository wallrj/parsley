import unittest

from parsley import termMaker as t

from namedconf import NamedConfParser as NCP



class NamedConfParserTests(unittest.TestCase):

    def test_directiveWithoutValue(self):
        """
        A directive without a value returns a None value.
        """
        self.assertEqual(
            NCP("mydirective;").directive(), ('mydirective', None))


    def test_directiveWithValue(self):
        """
        A directive with a quoted value returns the unquoted value.
        """
        self.assertEqual(
            NCP("mydirective 'myvalue';").directive(),
            ('mydirective', 'myvalue'))


    def test_directive(self):
        """
        A directive with a quoted value returns the unquoted value.
        """
        self.assertEqual(
            NCP("mydirective 'myvalue';").directive(),
            ('mydirective', 'myvalue'))


    def test_statementEmpty(self):
        """
        A statement may not contain any content.
        """
        self.assertEqual(
            NCP("mystatement { }").statement(),
            t.Element('mystatement', []))


    def test_statementWithDirective(self):
        """
        A statement may contain directives.
        """
        self.assertEqual(
            NCP("mystatement { mydirective; }").statement(),
            t.Element('mystatement', [('mydirective', None)]))
