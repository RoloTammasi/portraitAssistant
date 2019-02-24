import csv
import os
main_folder_name = "StudentFolders"

# open CSV as read and binary
f = open('sj_sample.csv', 'rb')

# put each row of the CSV in an array
reader = csv.reader(f)

# go through each row of CSV array
for row in reader:
    
    # length of "last name" row greater than 0
    # do not match if the cell = "last name"
    if len(row[0]) > 0 and row[0] != "Last name":
        name = main_folder_name + "/" + row[0] + " " + row[1] + " " + row[5]
        os.makedirs(name)
"""
        # if there is more than one child
        if "," in row[1]:
            child_names = row[1].split(", ")
            print("child_names: " + str(child_names))
            for child in child_names:
                child_name_subfolder = name + "/" + child
                os.makedirs(child_name_subfolder)
    
        # if there is one child
        else:
            child_name = row[1]
            child_name_subfolder = name + "/" + child_name
            os.makedirs(child_name_subfolder)
"""
f.close()

