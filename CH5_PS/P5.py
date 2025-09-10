''' create an empty disctionary . Allow user to input names as key and favorite subject as values 
and assume that the names are unique'''

hemlo={}

n1=input("Enter name 1  :\t")
lang1= input("Enter favorite language  :\t")
hemlo.update({n1:lang1})

n2=input("Enter name 2  :\t")
lang2= input("Enter favorite language  :\t")
hemlo.update({n2:lang2})

n3=input("Enter name 3  :\t")
lang3= input("Enter favorite language  :\t")
hemlo.update({n3:lang3})

n4=input("Enter name 4  :\t")
lang4= input("Enter favorite language  :\t")
hemlo.update({n4:lang4})

print(hemlo)

'''if two names(key) are same but the value is diffent ,
 the updated method change its values and key reamin constant   
 '''
# keys(identifire) can not be same but value does 


