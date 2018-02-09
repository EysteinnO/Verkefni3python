# -*- coding: cp1252 -*-
from bottle import *
import os

#frettir = ['Hallo', 'Hallo2', 'Hallo3', 'Hallo4']
frettir = [['Hallo', 'Þetta er texti við frétt númer 1', 'eysteinn@mbl.is'],['Hallo2', 'Þetta er texti við frétt númer 2', 'dsg@mbl.is']]
frettstring = str(frettir)

@route('/staticskrar/<skra>')

def staticskrar(skra):
    return static_file(skra, root='./myndir')
    
@route('/')
def index():
    return template('index.tpl')


    
@route('/frett/<id>')
def index(id):
        return template('frett.tpl', id=id,f=frettir),  

@error(404)
def villa(error):
    return "<br><h1>Þessi síða er ekki til</h1>"

run()
