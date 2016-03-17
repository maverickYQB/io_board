#!/usr/bin/env python
'''
Created on Mar 15, 2016
This app is mean to be used with the io_board
@author: maverickYQB
'''

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    boards= {"item_1":"board_1", "item_2":"board_2"}
    for board in boards:
        print boards[board]
    return render_template('layout.html',boards = boards)


@app.route('/boards')
def input_list():
    inputs = {
    "input_1":{"type":"analog","scale_range":"temp","ad_value":"511","present_value":"26'C"},
    "input_2":{"type":"analog","scale_range":"temp","ad_value":"2016","present_value":"55'C"}
    }

    for key, value in sorted(inputs.iteritems()):
        print key
        print value
        for i, j in value.iteritems():
            print i,j




if __name__ == '__main__':
    input_list()
    #app.run()