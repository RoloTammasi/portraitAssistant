#!/usr/bin/env python
# coding: utf-8

import pyqrcode
import pandas as pd
import os

# set variable(s)
QR_folder = "test_data/QRs"
student_CSV = "test_data/sj_sample.csv"
last_name_row = "Last name"
first_name_row = "First name"
student_id_row = "Student ID"


def createQR(student):
    
    qr = pyqrcode.create(student)
    qr.png(QR_folder + "/" + student + ".png", scale=20)

    
# create folder to store QRs
os.mkdir(QR_folder)

# import student data
students = pd.read_csv(student_CSV)

# create QR for every student
for index, row in students.iterrows():
    createQR(row[last_name_row] + row[first_name_row] + str(row[student_id_row]))
