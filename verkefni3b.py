# -*- coding: cp1252 -*-
from bottle import *

route('/sida')

def index():
    return template('index.tpl')

run()
