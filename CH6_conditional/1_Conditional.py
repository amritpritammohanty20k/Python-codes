# IF/ELSE STATEMENT.....
# The space before any conditional statement is called "INDENT"
'''
SYNTAX:-

if(condition):
else(statement):

'''
x=int(input("Enter your age  :")) #type: ignore

if(x>=18):
    print("YOU ARE ELIGIBLE FOR VOTE") 

else:
    print("YOU ARE NOT ELIGIBLE FOR VOTE") 

#ELIF STATEMENT / IF,ELSE,ELIF LADDER .....
'''
SYNTAX:-

if(condition):
elif(condition):
else:(statement)    
    
 if IF (F) thn ELIF will work , we can add multiple of it.   
    
    
    '''
x1=int(input("Enter your age  :")) #type: ignore

if(x1>=18):
    print("YOU ARE ELIGIBLE FOR VOTE")

elif(x1<0):
    print("INVALIDE INPUT ! NEGATIVE AGE IS NOT SUPORTED")
elif(x1==0):
    print("INVALIDE INPUT ! AGE CAN'T BE 0 !!!")

else:
    print("YOU ARE NOT ELIGIBLE FOR VOTE")