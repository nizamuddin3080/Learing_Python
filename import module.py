# This is the code for the online based coelenterates of the class number 9

import datetime


class MessageUser:
    user_details = []
    message = []
    base_message = """
                        Hi thank you for purchasing on {date}.
                        we hope you are exiting about to using this 
                        just a reminder to purchase this total amount of ${total}.
                        Have a great o ne 
                        
                        team CFC
                    """

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % amount
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail["date"] = date_text
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.message.append(new_msg)
                return self.message
            return []


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

# default_name = ["alim", "rabbi", "akash", "adib", "sabbir", "likhon", "ontu"]
# default_amount = [12, 54, 87, 85, 67, 57, 49]
