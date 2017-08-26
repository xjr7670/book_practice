import unittest
from country_codes import get_country_code

class TestCountryCode(unittest.TestCase):
    """用于测试country_codes.py"""

    def test_get_country_code(self):
        code = get_country_code("Andorra")
        self.assertEqual(code, "ad")

unittest.main()
