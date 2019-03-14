import context
from src import FooBar

from unittest import TestCase


class FooBarTestCase(TestCase):
    
    def test_foo_bar(self):
        self.assertEqual(FooBar().return_foo(), "foo")