""" Find a student is passed or failed ,
if it requires total 50% and at least 35% in each subject to pass , 
assume 3 subject and take as an input from the user !
"""
s1=int(input("Mark in Enlish:  \t")) # type:ignore
s2=int(input("Mark in Mathematics:  \t")) # type:ignore
s3=int(input("Mark in Science:  \t")) # type:ignore




total_percentage=(100*(s1+s2+s3))/300
print(f"\nTotal Percentage: {total_percentage:.2f}%")

if(total_percentage>=50):
    print("YOU ARE PASSED")
else:
    print("YOU ARE FAILED")