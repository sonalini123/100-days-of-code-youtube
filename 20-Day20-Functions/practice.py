# def name (a ,b):
#     print("Hello", a ,b)

# name("Sona", "Anand")    

def calculateGmean(a,b):
    gmean = (a*b)/(a+b)
    print(gmean)

def isgreater(a,b):
    if (a>b):
        print("first number is greater")
    else:
        print("second number is greater")

def islesser(a,b):
    if(a<b):
        print("first number is less than second")
    else:
        print("second number is smaller")

a=9
b=8
isgreater(a,b)
calculateGmean(a,b)