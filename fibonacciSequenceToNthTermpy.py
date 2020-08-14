# program to output the fibonacci sequence of a given number

numOfTerms = int(input("Enter a valid number : "))

#initialising variables

num1 = 0
num2 = 1
count = 0

#check if number entered is a valid number

if noOfTerms <= 0:
    print("Please enter a valid number: ")
elif numOfTerms == 1:
    print("The fibonacci sequence is: ", numOfTerms)
    print(num1)
else:
    print("The fibonacci sequence is: ")
    while count < numOfTerms:
        print(num1)
        term = num1 + num2

#update new values of variables

        num1 = num2
        num2 = term
        count += 1
