import json
import os
from flask import Flask, make_response, request, redirect, url_for, send_from_directory
import pandas as pd
import charges.charges as charges
import computer.computer as computer
import triangle.triangle as triangle
import thecalendar.thecalendar as thecalendar
from flask_cors import CORS


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/triangle', methods=['POST', 'GET'])
def question1():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    df[7] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = triangle.judge(df[1][i], df[2][i], df[3][i])
        df.loc[i, 6] = triangle.compute(df[1][i], df[2][i], df[3][i])
        if str(df[4][i]) != str(df[6][i]):
            df.loc[i, 7] = "未通过"
        else:
            df.loc[i, 7] = "通过"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/telecom', methods=['POST', 'GET'])
def question2():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[4] = 0
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 4] = charges.count(df[1][i], df[2][i])
        df.loc[i, 5] = charges.compute(df[1][i], df[2][i])
        if str(df[3][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)
    return response


@app.route('/computer', methods=['POST', 'GET'])
def question3():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = computer.compute(df[1][i], df[2][i], df[3][i])
        if str(df[4][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


@app.route('/calendar', methods=['POST', 'GET'])
def question4():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = thecalendar.calendar_atom([df[1][i], df[2][i], df[3][i]])
        if str(df[4][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')