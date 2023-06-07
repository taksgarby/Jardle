import unittest
from jardle import Jardle

class TestJardle(unittest.TestCase):

    def setUp(self):
        self.jardle = Jardle("えんぴつ")

    def test_game_has_secret_word(self):
        self.assertEqual("えんぴつ", self.jardle.secret)
    
    def test_user_can_make_a_guess(self):
        self.jardle.attempt("えんそく")
        self.assertEqual(1, len(self.jardle.attempts))
    
    def test_game_has_remaining_attempts(self):
        self.jardle.attempt("えんそく")
        self.assertEqual(5, self.jardle.remaining_attempts)