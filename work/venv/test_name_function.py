import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试函数工作"""

    def test_first_last_name(self):
        """能正确处理像Janis Joplin的姓名"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够处理中间名"""
        formatted_name = get_formatted_name('wolfgang','mozart',
                                            'amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()