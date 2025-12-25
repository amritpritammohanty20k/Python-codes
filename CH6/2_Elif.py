x=int(input("Enter your age:   ")) #type:ignore

if(x>=18):
    print("\tYOU ARE ELIGIBLE FOR VOTE !\t")
    if (x<18):
        print("\tYOU ARE NOT ELIGIBLE FOR VOTE !\t")
elif(x==0):
    print("\tAGE CAN'T BE ZERO\t")
elif(x<0):
    print("\tINVALIDE INPUT\t")
else:
    print("!!! DO NOT VOTE AGAIN !!!")
