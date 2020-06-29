class mathematical_operations:

    pi = 3.14

    def __init__(self, lenght, breadth, height, radius):
         self.lenght = lenght
         self.breadth = breadth
         self.height = height
         self.redius = radius

    def area_of_square(self):
        #self.lenght = lenght
        area = self.lenght * self.lenght
        print(f"Area of Square : {area}")
        return area

    def are_of_rectangle(self,length, breadth):
        self.lenght = lenght
        self.breadth = breadth
        area = self.lenght * self.breadth
        print(f"Area of Rectangle : {area}")
        return area

    def area_of_circle(self, radius):
        print(mathematical_operations.pi)
        self.radius = radius
        area_circle = mathematical_operations.pi * radius * radius
        print(f"Area of circle : {area_circle}")
        return area_circle

    def volume_of_cylinder(self):
        volume = mathematical_operations.pi * self.radius * self.radius * self.height
        print(f"Volume of Cylinder is {volume}")
        return volume


mo = mathematical_operations(3,4,5,6)
operation = int(input("Enter your choice: \n"
                  "1. Area of Square \n"
                  "2. Area of Rectangle \n"
                  "3. Area of Circle \n"
                  "4. Volume of Cylinder \n"))

if operation == 1:
    print("In 1")
    lenght = int(input("Enter the Lenght: "))
    mo.area_of_square()
elif operation == 2:
    lenght = int(input("Enter the Lenght: "))
    breadth = int(input("Enter the Breadth: "))
    mo.are_of_rectangle(lenght,breadth)
elif operation == 3:
    print(type(mathematical_operations.pi))
    radius = int(input("Enter the Radius: "))
    mo.area_of_circle(radius)
elif operation == 4:
    radius = int(input("Enter the radius: "))
    height = int(input("Enter the height: "))
    mo.volume_of_cylinder()

else:
    print("Please enter a relevant choice")



