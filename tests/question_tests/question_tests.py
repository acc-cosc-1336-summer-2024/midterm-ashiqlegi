#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import is_prime
from src.question_b.question_b import get_person_category
from src.question_c.question_c import get_miles_per_hour
from src.question_d.question_d import get_sum_of_evens
class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))

    def test_question_b_config(self):
        self.assertEqual("infant", get_person_category(1))
        self.assertEqual("child", get_person_category(2))
        self.assertEqual("teenager", get_person_category(14))
        self.assertEqual("adult", get_person_category(20))

    def test_question_c_config(self):
        self.assertEqual(19.883872, get_miles_per_hour(32,60))

    def test_question_d_config(self):
        self.assertEqual(30, get_sum_of_evens(11))
        self.assertEqual(30, get_sum_of_evens(10))
        self.assertEqual(20, get_sum_of_evens(8))
        