# import csv          #csv = comma separated value

# with open("data.csv", "w+") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Title", "Description", "col-3"])
#     writer.writerow(["row_1", "some descr.", "Another"])
#     writer.writerow(["row_1", "some descr.", "Another"])
#     writer.writerow(["row_1", "some descr.", "Another"])
#     writer.writerow(["row_1", "some descr.", "Another"])




# with open("data.csv", "a") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["appand", "Description", "col-3"])


#import csv 

# with open("data.csv", "w+") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["col-1", "col-2"])
#     writer.writerow(["data-1", "data-2"])
#     writer.writerow(["data-3", "data-4"])


# with open("data.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


# with open("data.csv", "w") as csvfile:
#     fieldnames = ["id", "Title"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({"id": 123, "title": "new title"})



import datetime

def main():
    DOB=input("Enter your DOB:")
    YearNow=datetime.datetime.now().year
    MyAge=YearNow-int(DOB)
    print("Your age is {} Year".format(MyAge))