# -*- coding: cp1252 -*-
from bottle import *
import os

ktlist1 = [1,2,3,4,5,6,7,8,9]
ktliststring1 = str(ktlist1)
ktsum1 = sum(i for i in ktlist1)

ktlist2 = [2,3,4,5,6,8,4,6,7]
ktliststring2 = str(ktlist2)
ktsum2 = sum(i for i in ktlist2)

ktlist3 = [4,5,7,8,9,4,3,2,1]
ktliststring3 = str(ktlist3)
ktsum3 = sum(i for i in ktlist3)



kt1 = str(ktsum1)
kt2 = str(ktsum2)
kt3 = str(ktsum3)


@route('/')
def index():
    return "<div><h1> Verkefni 3 </h1><ul style='list-style-type:square'><li><p>Gunnar Gunnarsson</p><a href='/sida/sida1'>",ktliststring1,"</a></li><li><p>Jón Jónsson</p><a href='/sida/sida2'>",ktliststring2,"</a></li><li><p>Jónatan Jónatansson</p><a href='/sida/sida3'>",ktliststring3,"</a></li></li></ul></div>"      


    

@route('/sida/<id>')
def index(id):

    if id == "sida1":        
        return "<h1> Þversumma </h1></b><p>Þversumma kennitölunnar ",ktliststring1," er </p>" , kt1
    if id == "sida2":
        return "<h1> Þversumma </h1></b><p>Þversumma kennitölunnar ",ktliststring2," er </p>" , kt2
    if id == "sida3":
        return "<h1> Þversumma </h1></b><p>Þversumma kennitölunnar ",ktliststring3," er </p>" , kt3
               
    
def page():
    l = request.query.nr   


@route('/myndir/<nafn>')
def myndir_static(nafn):
    return static_file(nafn,root='myndir')

@error(404)
def villa(error):
    return "<br><h1>Þessi síða er ekki til</h1>"


run()
#run(host='0.0.0.0', port=os.environ.get('PORT'))
