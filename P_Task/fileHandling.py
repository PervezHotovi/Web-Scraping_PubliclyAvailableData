#CSV is stand for Comma separated values , it is a type of plan text file, in which data are present in the form of  rows and columns each separated with commas.

import csv
import re
with open("test.csv", mode="w+" , newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["ID", "Name"])
    writer.writerow(["323", "Pervez"])
    writer.writerow(["983","Abbas"])
with open("test.csv", "r") as file:
    print(file.read())

with open("test.csv", "a", newline="") as file:
    file.write("Thank you")


with open("test.csv", "r" ) as file:
    print(file.read())



# f = open("myFile.txt", "w")
# con="my name is pervez Abbas"
# text=f.write(con)
# f.close()
# with open("myFile.txt", "a+") as f:
#     text= f.write("Thank you")

# f=open("myFile.txt", "r")
# print(f.read())
c=0

with open("myFile.txt", "r") as file:
    text=file.read()
    pattern="^[d]"
    file_text= text.split()
    find_words=[]
    for w in file_text:
       
        if (re.findall(pattern, w)):
            find_words.append(w)
            c+=1
if c==0:
    print("No such word in the file")
else:
    print(find_words)


