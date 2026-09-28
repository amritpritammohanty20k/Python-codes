# "Build and learning the logic of the 'SMART FIND'"


# Multiple condition with "AND"
"""
if condition1 and condition2:
(executes when both condition are true ) (and = 2T)
EX:
"""
# and 
item_type = "watch"
colour = "black"

if item_type == "watch" and colour == "black":
    print("Possible match")

# or
item_status = "Found"
claim_status = "Avaliable"

if item_status == "Found" or claim_status == "Avaliable":
    print("You can submit a claim")
else:
    print("This item can not be claimed")

"One of the condition must be TRUE for succesfull executation"

# not (T to F viseversa)
item_return = False

if not item_return:
    print("Item is still active")

# and or not 
# Context: if the admin blocked some one then the user can't logged into using same id
role = "student"
logged_in = True
acc_blc = False

if logged_in and not acc_blc:
    print("Account access allowed ")

"Parenthesis in Complex condition"
''' if logged_in and (role == "admin" or role == "security"):'''
# Context: read it as Is this user login ?  AND Admin or Security ?

# Code 1

item_available = True
user_id = True
finder_id = False   ("user id n finder id are  only for demo code to work ")


if logged_in and item_available and (user_id != finder_id):
    print("U can claim the item ")
else:
    print("Can't be claimed ")