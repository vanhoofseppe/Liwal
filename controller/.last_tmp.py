#-*-coding:utf8;-*-
#qpy:3
#Liwal WebApp
#http://localhost:8080/
"""
main.py
"""
from bottle import route, run, template, TEMPLATE_PATH

#TEMPLATE_PATH.insert(0, '/storage/emulated/0/qpython/projects3/Liwal/views')

@route('/')
def home():
    return template('home.html')

run(host='10.0.0.57', port=8080)