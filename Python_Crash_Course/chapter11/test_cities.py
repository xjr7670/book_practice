import unittest
from city_functions import get_city_country

class Test_City_Country(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """是否能正确处理像Guangzhou, China这样的城市"""
        formatted_city = get_city_country('guangzhou', 'china')
        self.assertEqual(formatted_city, "Guangzhou, China")

    def test_city_country_population(self):
        """测试是否能正确处理加上人口后的信息"""
        formatted_city = get_city_country('santiago', 'chile', 'population=5000000')
        self.assertEqual(formatted_city, "Santiago, Chile - Population=5000000")

unittest.main()
