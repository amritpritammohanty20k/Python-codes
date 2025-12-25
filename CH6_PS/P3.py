# A spam comment is defined as a text containing following keywords-
#"make a lot of money","buy now","suscribe this","click this"
#Write a program to detect this spam

""" CTREATE A SPAM FILTER"""


a="make a lot of money"
b="buy now"
c="suscribe this"
d="click this"

message=input("Enter your comment: ") #type:ignore

if((a in message) or (b in message) or (c in message) or (d in message)):
    print("spam")
else:
    print("not spam")