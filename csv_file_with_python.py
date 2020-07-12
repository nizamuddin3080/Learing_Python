import csv          #csv = comma separated value

with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Description"])
    writer.writerow(["row_1", "some descr."])



