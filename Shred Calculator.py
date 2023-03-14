## This code is built to calculate goals for weight loss and body fat percentage
##Credit to Jeremy Ethier for the body weight algorithm
import math
def Shred_Calculator(User_Weight,User_BF,Goal_BF):
    Total_Fat=float(User_Weight*(User_BF/100))
    Lean_Mass=float(User_Weight-Total_Fat)
    Goal_Weight=float(Lean_Mass/(1-(Goal_BF/100)))
    return Goal_Weight
def menu():
    print("WELCOME TO THE SIX PACK CALCULATOR\n1 Press 1 to start \n2 press 2 to quit \n3 press 3 for calculator advice")
    User_Choice=str(input("Enter a choice:"))
    while not User_Choice.isnumeric():
        print("Please enter a number")
        User_Choice= input("Try again:")
    return User_Choice
def Fail_Safe(x,y):
    while not x.isnumeric():
        print("Please enter a numerical value for your"+y)
        x=input("Try again: ")
    return x
               
        

def main():
    while True:
        User_Choice=menu()
        if User_Choice == str(1):
            User_Weight=Fail_Safe(input("Please enter your body weight: ")," body weight")
            User_BF=Fail_Safe(input("Please enter your body fat percentage: ")," body fat")
            Goal_BF=Fail_Safe(input("Please enter your goal body fat percentage: ")," goal body fat")
            Final_Output=Shred_Calculator(float(User_Weight),float(User_BF),float(Goal_BF))
            print("To be "+ str(User_BF)+" percent body fat, you need to be %.2f " %Final_Output + " pounds")
        elif User_Choice== str(2):
            print("thank you for using the SIX PACK CALCULATOR, goodbye!")
            break   
        elif User_Choice== str(3):
            print("The general body fat percentage to be considered 'shredded' is 15 percent, however the lower, the more shredded you will look.")


main()
        


