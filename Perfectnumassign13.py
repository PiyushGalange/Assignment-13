# Write a program to accept number from user and print whether it is a perfect number or not.

def main():

    Num = int(input("Enter a Number : "))
    Sum = 0
    for i in range(1, Num):
        if(Num % i == 0):
            Sum = Sum + i
            total_sum = Sum
            
    print(total_sum)

    if(total_sum == Num):
        print("Ohh its a  -- Perfect num")
    else:
        print("Not a Perfect num")
        


if __name__ == "__main__":
    main()