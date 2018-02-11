# -*- coding: cp1252 -*-
from bottle import *
import os

#frettir = ['Hallo', 'Hallo2', 'Hallo3', 'Hallo4']
frettir = [['St�rhr�� og stormur � v�ndum', 'Brjala� ve�ur alla helgina.', 'eysteinn@mbl.is', 'stormur.jpg'],['�k � mann og sparka�i � hann', 'L�g�regl�unni � h�fu�borg�ar�sv��inu barst um klukk�an 17 � g�r�dag til�kynn�ing um �ku�mann b�ls sem haf�i eki� utan � mann vi� Gar�astr�ti � Reykja�v�k. �kuma�ur�inn er s��an sag�ur hafa st��va� b�l�inn, fari� �t �r hon�um, hr�pa� a� mann�in�um og sparka� � hann. �� er hann einnig sag�ur hafa reynt a� sl� til hans.', 'dsg@mbl.is','police.jpg'],['H�r er pl�ss fyrir miklu fleiri', '�H�r er pl�ss fyr�ir miklu fleiri en kerfi� er svo svifa�seint. � me�an veri� er a� fara yfir papp��ra og skj�l sef�ur f�lk � ruslageymsl�um og � bekkj�um,� seg�ir Svan�ur El�as�son, �b�i � V��inesi sem er ney�ar�r�r��i Reykja�v�k�ur�borg�ar fyr�ir h�s�n��is�laust f�lk.', 'gunni@mbl.is','plass.jpg'],['Greip � tomt � ap�tekinu','Lyf sem er nau�syn�legt �tta �ra g�mlu barni er ekki til hj� lyfja�heild�s�l�unni � �eim styrk�leika sem �a� �arf a� f�. Lyfi� g�ti veri� f�an�legt � ein�hverj�um ap�tek�um, sam�kv�mt upp�l�s�ing�um fr� Lyfja�stofn�un, en �� ekki alls sta�ar, t.d. � �eim ap�tek�um �ar sem barni� b�r. M��ir �ess greip �v� � t�mt �egar h�n �tla�i a� s�kja fyr�ir�framp�anta�an skammt af lyf�inu � ap�tek � vik�unni. �ar f�kk h�n �au sv�r a� lyfi� v�ri hvergi til og k�mi ekki a.m.k. n�stu tv�r vik�urn�ar.','bubbi@mbl.is','tint.jpg']]
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
    return "<br><h1>�essi s��a er ekki til</h1>"

#run()
run(host='0.0.0.0', port=os.environ.get('PORT'))
