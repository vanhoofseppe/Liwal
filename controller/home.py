#-*-coding:utf8;-*-
#qpy:3
#Liwal WebApp
#http://localhost:8080/
"""
views/home.py
"""
from bottle import route, run, template
@route('/')
def home():
    return template('home.html')