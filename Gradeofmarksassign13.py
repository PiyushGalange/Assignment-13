# Write a program which accepts marks and displays its Grade

#Conditions:

#>= 75 -> Distinction
#>= 60 -> First class
#>= 50 -> Second class
#< 50 -> Fail

def main():

    Marks = int(input("Enter the marks i will tell your Grade : "))

    if(Marks >= 75):
        print("*****Distinction*****")
    elif(Marks >= 60):
        print("****First Class****")
    elif(Marks >= 50):
        print("**Second Class**")
    else:
        print("Sorry yor are Fail")



if __name__ == "__main__":
    main()