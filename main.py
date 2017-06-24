#-*-coding:utf8;-*-
#qpy:3
#Liwal WebApp
#http://localhost:8080/
"""
main.py
"""
import json
from pprint import pprint
from bottle import route, run, template, TEMPLATE_PATH

with open('/storage/emulated/0/qpython/repos/Liwal/settings.json') as settings_file:
				settings = json.load(settings_file)

pprint(settings)

TEMPLATE_PATH.insert(0, settings['root_path'] + 'views')

import controller.home

run(host=settings['host'], port=settings['port'])