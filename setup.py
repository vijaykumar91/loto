import sys
import pandas as pd
from flask import Flask, escape, request,render_template
import xlrd
import redf = pd.read_excel(r'C:\Users\RELIANCE DIGITAL\PycharmProjects\loto\5_16_read_excel.xlsx', header=None, index=None)

loc = (r'C:\Users\RELIANCE DIGITAL\PycharmProjects\loto\5_16_read_excel.xlsx')  # write URL path
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# print(sheet.cell_value(1, 0))

url = (sheet.cell_value(1, 0))  # 5 - denote URL number
print((url)

)

url1 = '11 21 22 32 47 21'

r = url1.split(' ', 6)
print(r)
re.split('\s+', url1)
print(r)
