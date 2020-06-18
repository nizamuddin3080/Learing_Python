from import_module import MessageUser, some_random, make_messages

obj = MessageUser()
obj.add_user("alim", 12, email='hello@cmtv.com')
obj.add_user("rabbi", 54)
obj.add_user("akash", 87)
obj.add_user("adib", 85)
obj.add_user("sabbir", 67)
obj.add_user("likhon", 57)
obj.add_user("ontu", 49)
obj.get_details()
obj.make_messages()

# print(obj.make_messages())
# some_random()

default_name = ["alim", "rabbi", "akash", "adib", "sabbir", "likhon", "ontu", "nowsad"]
default_amounts = [12, 54, 87, 85, 67, 57, 49, 67]

make_messages(default_name, default_amounts)