# Author Sergio Guerrero 
# date 03/17/2020

#importing modules from other files
import lib
import loyalty
# importing a class from a module and assigning alias
#from Shockwave import ShockwaveClass as sw

print('starting py code')
print("")

#provide a name to return Hello World or pass empty to get an error messgae
print(lib.sayHello("Sergio"))

# calling two functions in the same module, passing a list (array does not exist in pythyon) 
# see str() --> conversion to string or int() conversion to integer or float()

#valAddAll = lib.addList([1,2,3,4,5,6])
#sumOfN = lib.sumOfNNumbers(6)
#print( "same value " + str(sumOfN) if(valAddAll == sumOfN) else " values are not the same " + str(valAddAll) + " vs " + str(sumOfN) )

""" # block comment
    # uncomment to call loyalty module and execute a select query against mssql
print("")
print("get loyalty customers")
custs = loyalty.getCustomers()

for c in custs:
    print(c)
"""
print("")

print("Calling my class Shockwave")
print(sw.getPerson(1))

# end of code
print("")
print('ending py code')
