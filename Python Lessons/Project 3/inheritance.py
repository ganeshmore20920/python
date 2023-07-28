class polygon:
    def __init__(self , sides):
        self.sides = sides
    def display_info(self):
        print("A Polygon is 2 dimensional shape with straight line ")
    def get_perimeter(self):
        perimeter = sum(self.sides)
        print(perimeter)
class Triangle(polygon):
    def display_info(self):
        print("A triangle is polygon with 3 edges ")
        
    def get_perimeter(self):
        perimeter = sum(self.sides)
        print(perimeter)
        super().get_perimeter()
class quadrilateral(polygon):
    def display_info(self):
        return super().display_info()

t1 = Triangle([5,6,6])
t1.get_perimeter()
t2 = Triangle([3,6,9])
t2.get_perimeter()
q1 = quadrilateral([1,2,3,4,5])
q1.get_perimeter()