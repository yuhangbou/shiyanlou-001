#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template 
import json
app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
@app.route('/')
def index():
    with open('/home/shiyanlou/files/helloshiyanlou.json') as file:
        file_shiyanlou=json.loads(file.read())
    with open('/home/shiyanlou/files/helloworld.json') as file:
        file_world=json.loads(file.read())
    title={} 
    title['helloshiyanlou']=file_shiyanlou['title']
    title['helloworld']=file_world['title']
    return render_template('index.html',title=title)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
@app.route('/files/<filename>')
def file(filename):
    with open('/home/shiyanlou/files/'+filename+'.json') as file:
        file_value=json.loads(file.read())
    return render_template('file.html',file_value=file_value)
if __name__=='__main__':
    app.run(
            host='127.0.0.1',
            port=3000,
            debug=True
            )



