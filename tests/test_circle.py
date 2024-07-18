import unittest
from shapes.circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), 3.14159, places=5)
