#conditional statements
#if if else elif
from webbrowser import open_new

#age>=18

age=10
if age>=18:

    print("Eligible to vote")
else:
    print("Not eligible to vote")

if False :
    print("true condition")
else:
    print("false condition")


height=4
if height>=6:
    print("Height is good")
else:
    print("Height is not good")

    a=5
    {print("hello"),print("python")} if a>=10 else {print("hi"),print("java")}


weekno=1

    if weekno==1:
        print("sunday")
    elif weekno==2:
        print("monday")
    elif(weekno==3):
        print("tuesday")
    elif weekno==4:
        print("Wednesday")
    elif weekno==5:
        print("Thursday")
    elif weekno==6:
        print("Friday")
    else:
        print("Invalid week number")