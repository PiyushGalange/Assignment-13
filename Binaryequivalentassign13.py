# Write a program which accepts a number and print its binary equivalent.

def main():

    Num = int(input("enter a Number : "))
    
    Binary = ""
    
    while Num > 0:

        Remain = Num % 2
        Binary = Binary + str(Remain)
        Num = Num // 2

    print(Binary)    


if __name__ == "__main__":
    main()
