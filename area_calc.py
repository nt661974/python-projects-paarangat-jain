print("Choose from the list of shapes: ")
print("Square (1)")
print("Rectangle (2)")
print("Trapezium (3)")
shape = input("Enter your input please: ")

match shape:
    case "1":
        side=int(input("Enter Side of Square: "))
        area = side*side
    case "2":
        side1=int(input("Enter length of the rectangle: "))
        side2=int(input("Enter height of the rectangle: "))
        area = side1*side2;
    case "3":
        bottom_width=int(input("Enter the bottom width of the trapezium: "))
        top_width=int(input("Enter the top width of the trapezium: "))
        height=int(input("Enter the height of the trapezium"))
        area=bottom_width*top_width*height

        
print("/n")
print("The total area is: " + str(area) + " units^2")
