import unittest
from area import *

class MyTestCase(unittest.TestCase):

    D_V = 0.0001

    def test_circle(self):
        self.assertAlmostEqual(circle(5), 78.5398, delta=self.D_V)
        self.assertAlmostEqual(circle(3.3333), 34.9059, delta=self.D_V)
        self.assertAlmostEqual(circle('2'), 12.5664, delta=self.D_V)
        self.assertAlmostEqual(circle('8.954'), 251.8744, delta=self.D_V)
        self.assertAlmostEqual(circle('     4.8    '), 72.3823, delta=self.D_V)
        self.assertAlmostEqual(circle('3e2'), 282743.3388, delta=self.D_V)
        self.assertRaises(ValueError, circle, '')
        self.assertRaises(ValueError, circle, 'hello')
        self.assertRaises(TypeError, circle, [1, 2, 3])
        self.assertRaises(TypeError, circle, {4, 5, 6})
        self.assertRaises(TypeError, circle, '-2')
        self.assertRaises(TypeError, circle, 0)


    def test_square(self):
        self.assertAlmostEqual(square(5), 25.0, delta=self.D_V)
        self.assertAlmostEqual(square(3.3333), 11.1109, delta=self.D_V)
        self.assertAlmostEqual(square('2'), 4, delta=self.D_V)
        self.assertAlmostEqual(square('8.954'), 80.1741, delta=self.D_V)
        self.assertAlmostEqual(square('     4.8    '), 23.04, delta=self.D_V)
        self.assertAlmostEqual(square('3e2'), 90000.0, delta=self.D_V)
        self.assertRaises(ValueError, square, '')
        self.assertRaises(ValueError, square, 'hello')
        self.assertRaises(TypeError, square, [1, 2, 3])
        self.assertRaises(TypeError, square, {4, 5, 6})
        self.assertRaises(TypeError, square, '-2')
        self.assertRaises(TypeError, square, 0)


    def test_rectangle(self):
        self.assertAlmostEqual(rectangle(4, 6), 24.0, delta=self.D_V)
        self.assertAlmostEqual(rectangle(4.5, 8.6), 38.7, delta=self.D_V)
        self.assertAlmostEqual(rectangle(4.5, 6), 27.0, delta=self.D_V)
        self.assertAlmostEqual(rectangle(4, 8.6), 34.4, delta=self.D_V)
        self.assertAlmostEqual(rectangle("5", 6), 30.0, delta=self.D_V)
        self.assertAlmostEqual(rectangle(4, "5.5"), 22.0, delta=self.D_V)
        self.assertAlmostEqual(rectangle("5", "5.5"), 27.5, delta=self.D_V)
        self.assertAlmostEqual(rectangle("    2    ", "        9"), 18.0, delta=self.D_V)
        self.assertAlmostEqual(rectangle("4e3", "5e4"), 200000000.0, delta=self.D_V)
        self.assertRaises(ValueError, rectangle, '', '')
        self.assertRaises(ValueError, rectangle, 'hello', 'world')
        self.assertRaises(ValueError, rectangle, 'hello', 3)
        self.assertRaises(ValueError, rectangle, 1, 'world')
        self.assertRaises(TypeError, rectangle, [1, 2, 3], 5)
        self.assertRaises(TypeError, rectangle, 7, {4, 5, 6})
        self.assertRaises(TypeError, rectangle, '-2', '5')
        self.assertRaises(TypeError, rectangle, '-2', '-1')
        self.assertRaises(TypeError, rectangle, '-2', -1)
        self.assertRaises(TypeError, rectangle, -2, -1)
        self.assertRaises(TypeError, rectangle, 0, 7)
        self.assertRaises(TypeError, rectangle, 7, 0)
        self.assertRaises(TypeError, rectangle, 0, 0)
        self.assertRaises(TypeError, rectangle, -5, 4)
        self.assertRaises(TypeError, rectangle, 3, -8)


    def test_triangle(self):
        self.assertAlmostEqual(triangle(4, 6), 12.0, delta=self.D_V)
        self.assertAlmostEqual(triangle(4.5, 8.6), 19.35, delta=self.D_V)
        self.assertAlmostEqual(triangle(4.5, 6), 13.5, delta=self.D_V)
        self.assertAlmostEqual(triangle(4, 8.6), 17.2, delta=self.D_V)
        self.assertAlmostEqual(triangle("5", 6), 15.0, delta=self.D_V)
        self.assertAlmostEqual(triangle(4, "5.5"), 11.0, delta=self.D_V)
        self.assertAlmostEqual(triangle("5", "5.5"), 13.75, delta=self.D_V)
        self.assertAlmostEqual(triangle("    2    ", "        9"), 9.0, delta=self.D_V)
        self.assertAlmostEqual(triangle("4e3", "5e4"), 100000000.0, delta=self.D_V)
        self.assertRaises(ValueError, triangle, '', '')
        self.assertRaises(ValueError, triangle, 'hello', 'world')
        self.assertRaises(ValueError, triangle, 'hello', 3)
        self.assertRaises(ValueError, triangle, 1, 'world')
        self.assertRaises(TypeError, triangle, [1, 2, 3], 5)
        self.assertRaises(TypeError, triangle, 7, {4, 5, 6})
        self.assertRaises(TypeError, triangle, '-2', '5')
        self.assertRaises(TypeError, triangle, '-2', '-1')
        self.assertRaises(TypeError, triangle, '-2', -1)
        self.assertRaises(TypeError, triangle, -2, -1)
        self.assertRaises(TypeError, triangle, 0, 7)
        self.assertRaises(TypeError, triangle, 7, 0)
        self.assertRaises(TypeError, triangle, 0, 0)
        self.assertRaises(TypeError, triangle, -5, 4)
        self.assertRaises(TypeError, triangle, 3, -8)







if __name__ == "__main__":
    unittest.main()