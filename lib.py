
# validating a simple string passed in, and an if statement 
def sayHello(name):
    errorMessage = "provide a name"
    outMessage = errorMessage if name == "" else "hello " + name    
    return outMessage

# validating a list passed in and a for loop
def addList(list):
    sumE = 0
    for item in list:
        sumE += item

    return sumE

# validating an int passed in and a formula output with data type conversion
def sumOfNNumbers(n):
    return int(( n * (n+1) ) / 2)    