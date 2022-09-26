from numpy import add_newdoc

def length_of_triangle(a,b,c):
    if a == b and b == c:
        return "Triangle is Equilateral"
    elif a == b and b == c or b == c and c != a or a == c and c != b:
        return "Triangle is Isosceles"
    elif a != b and b != c and c != a:
        return "Triangle is Irregular"
