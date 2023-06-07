import unittest
from jardle import Jardle

class TestJardle(unittest.TestCase):

    def setUp(self):
        self.jardle = Jardle("えんぴつ")

    def test_game_has_secret_word(self):
        self.assertEqual("えんぴつ", self.jardle.secret)