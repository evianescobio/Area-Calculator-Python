import math
# This is the heading of the program.
print("==================")
print("Area Calculator 📐")
print("==================\n")

# Display the menu.
while True: 
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit\n")
    
    # Ask the user to choose the shape.
    choice = int(input("Which shape: "))

    # Calculate and display the area of the triangle.
    if choice == 1:
        base = int(input("Base: "))
        height = int(input("Height: "))
        area = (base * height) / 2
        print(f"The area of the triangle is {area}\n")

    # Calculate and display the area of the rectangle.
    elif choice == 2:
          base = int(input("Base: ")
          height = int(input("Height: "))
          area = base * height
          print(f"The area of the rectangle is {area}\n")

    # Calculate and display the area of the square.
    elif choice == 3:
            side = int(input("Side: "))
            area = side ** 2
            print(f"The area of the square is {area}\n")

    # Calculate and display the area of the circle.
    elif choice == 4:
            radius = int(input("Radius: ")
            area = math.pi * (radius ** 2)
            print(f"The area of the circle is {area}\n")

    # Terminate the program if choice is 5.
    elif choice == 5:
        print("Goodbye!")
        break

    # Invalid Input.
    else:
        print("Invalid input. Please try again.\n\n")
    
            
            




