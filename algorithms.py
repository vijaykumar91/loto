from flask import Flask, escape, request,render_template
import pandas as pd
import xlrd
import re
import os


app = Flask(__name__)

@app.route('/')
def hello():

    return render_template('index.html')
    #return f'Hello, {escape(df)}!'


@app.route('/analysis',methods=['POST'])
def analysis():
    first = request.form['first']
    second = request.form['second']
    third = request.form['third']
    fourth = request.form['fourth']
    five = request.form['five']
    six = request.form['six']

    getInput=[]
    getInput.append(first)
    getInput.append(second)
    getInput.append(third)
    getInput.append(fourth)
    getInput.append(five)
    getInput.append(six)
    print('first==>>',(getInput))
    loc = (r'5_16_read_excel.xlsx')  # write URL path
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    row =sheet.nrows
    print('row 1',row)
    # print(sheet.cell_valu =  sheet.nrows # or wb.nsheets


    InputList={}
    #Digit List
    countDict={}
    for inputNumber in getInput:
        checkExistList = []
        #read number from sheet
        matchCount=0
        for rowsIndex in range(row):
            digitNumber = (sheet.cell_value(rowsIndex, 0))  # 5 - denote URL number
            digitNumber1 = digitNumber
            digitList = digitNumber1.split(' ', 6)

            if inputNumber in digitList:
                checkExistList.append(digitList)
                matchCount +=1
            countDict[inputNumber] = matchCount
            #print(inputNumber)
        InputList.update({inputNumber:checkExistList})
    print('countDict==>>',countDict)

    print('first==>>', type(first))
    print('first 123==>>', (first))
    firstMatch = countDict[first]
    second = countDict[second]
    third = countDict[third]
    fourth = countDict[fourth]
    five = countDict[five]
    six = countDict[six]

    input_2_with_six=0
    input_3_without_six = 0
    input_3_with_six = 0
    input_4_without_six = 0
    input_4_with_six = 0
    input_5_without_six = 0
    input_5_with_six = 0
    input_2 = 0

    allmatchedCount=len(list(filter(lambda num: num != 0, countDict.values()) ))

    print('six',six)
    print('allmatchedCount',allmatchedCount)
    countDictList=list(filter(lambda num: num != 0, countDict.values()))
    if allmatchedCount ==2 and six !=0:
        for x in countDictList:
            print('x==>',x)
            input_2_with_six += 10 * x

    print('input_2_with_six',input_2_with_six)
    #if in the numbers that the user input 3 of them are matched, WITHOUTthe sixth number, then you multiply the number of time that happens by 10
    if allmatchedCount ==3 & six ==0:
        for y in countDictList:
            input_3_without_six += 10 * y


    #if in the numbers that the user input 3 of them are matched, along with the sixth number matched too, then you multiply the number of time that happens by 200
    if allmatchedCount ==3 and six !=0:
        for z in countDictList:
            input_3_with_six += 200 * z


    #if in the numbers that the user input 4 of them are matched, WITHOUTwith the sixth number matched too, then you multiply the number of time that happens by 500
    if allmatchedCount ==4 & six ==0:
        for z in countDictList:
            input_4_without_six += 500 * z


    #if in the numbers that the user input 4 of them are matched, WITHOUTwith the sixth number matched too, then you multiply the number of time that happens by 500
    if allmatchedCount ==4 & six !=0:
        for m in countDictList:
            input_4_with_six += 10000 * m


    #if in the numbers that the user input 5 of them are matched, without with the sixth number matched too, then you multiply the number of time that happens by 1,000,000
    if allmatchedCount ==5 and six ==0:
        for n in countDictList:
            input_5_without_six += 1,000,000 * n



    # if in the numbers that the user input 5 of them are matched, along with the sixth number matched too, then print "YOU CAN QUIT YOUR JOB NOW"
    if allmatchedCount == 5 and six != 0:

        input_5_without_six = 'YOU CAN QUIT YOUR JOB NOW'



    return f'Result Of input values, !== input_2_with_six=> {input_2_with_six} ==! , ' \
           f'' \
           f'!== input_3_without_six=> {input_3_without_six} ==<=>\n ' \
           f'!== input_3_with_six=> {input_3_with_six} ==<=>\n ' \
           f'!== input_4_without_six=> {input_4_without_six} ==<=>\n '\
           f'!== input_4_with_six=> {input_4_with_six} ==<=>\n ' \
           f'!== input_5_without_six=> {input_5_without_six} ==<=>\n ' \
           f'!== input_5_with_six=> {input_5_with_six} ==<=>\n ' \
           f'' \
           f' {escape(InputList)}! {escape(countDict)}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)