import unittest
import triangleUtils

class triangleTest(unittest.TestCase):
    def test_triangle_equilateral(self):
        # Arrange
        a =int(2)
        b =int(2)
        c =int(2)
        expectedResult = str("Triangle is Equilateral")
        # Act
        result = triangleUtils.length_of_triangle(a,b,c)
        # Assert
        self.assertEqual(result,expectedResult)

    def test_triangle_isosceles(self):
        # Arrange
        a =int(2)
        b =int(5)
        c =int(5)
        expectedResult = str("Triangle is Isosceles")
        # Act
        result = triangleUtils.length_of_triangle(a,b,c)
        # Assert
        self.assertEqual(result,expectedResult)

    def test_triangle_irregular(self):
        # Arrange
        a =int(8)
        b =int(2)
        c =int(5)
        expectedResult = str("Triangle is Irregular")
        # Act
        result = triangleUtils.length_of_triangle(a,b,c)
        # Assert
        self.assertEqual(result,expectedResult)

if __name__ == "__main__":
    unittest.main()