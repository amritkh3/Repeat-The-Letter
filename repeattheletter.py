"""ask user to enter any word and return it with each character repeated. ex,
if user enter word "test" the execution must be "tteesstt" .

1.ask user to input any word and assign it to the variable string
2.run for loop in string 
 for index in string:
    print(inden+index,end="") 
"""


string=input("enter any word ")
for index in string:
    print(index+index,end="")
    
    

