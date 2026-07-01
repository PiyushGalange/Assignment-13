# write a program to accept radius of circle and print its area

def main():

    Radius = float(input("Enter the radius of a Circle : "))
    Pi = 3.14

    Area = Pi * (Radius*Radius)

    print("Area of Circle is : ",Area) 



if __name__ == "__main__":
    main()