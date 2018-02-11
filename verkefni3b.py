# -*- coding: cp1252 -*-
from bottle import *
import os

#frettir = ['Hallo', 'Hallo2', 'Hallo3', 'Hallo4']
frettir = [['Stórhríð og stormur í vændum', 'Brjalað veður alla helgina.', 'eysteinn@mbl.is', 'stormur.jpg'],['Ók á mann og sparkaði í hann', 'Lög­regl­unni á höfuðborg­ar­svæðinu barst um klukk­an 17 í gær­dag til­kynn­ing um öku­mann bíls sem hafði ekið utan í mann við Garðastræti í Reykja­vík. Ökumaður­inn er síðan sagður hafa stöðvað bíl­inn, farið út úr hon­um, hrópað að mann­in­um og sparkað í hann. Þá er hann einnig sagður hafa reynt að slá til hans.', 'dsg@mbl.is','police.jpg'],['Hér er pláss fyrir miklu fleiri', '„Hér er pláss fyr­ir miklu fleiri en kerfið er svo svifa­seint. Á meðan verið er að fara yfir papp­íra og skjöl sef­ur fólk í ruslageymsl­um og á bekkj­um,“ seg­ir Svan­ur Elías­son, íbúi í Víðinesi sem er neyðarúr­ræði Reykja­vík­ur­borg­ar fyr­ir hús­næðis­laust fólk.', 'gunni@mbl.is','plass.jpg'],['Greip í tomt í apótekinu','Lyf sem er nauðsyn­legt átta ára gömlu barni er ekki til hjá lyfja­heild­söl­unni í þeim styrk­leika sem það þarf að fá. Lyfið gæti verið fá­an­legt í ein­hverj­um apó­tek­um, sam­kvæmt upp­lýs­ing­um frá Lyfja­stofn­un, en þó ekki alls staðar, t.d. í þeim apó­tek­um þar sem barnið býr. Móðir þess greip því í tómt þegar hún ætlaði að sækja fyr­ir­framp­antaðan skammt af lyf­inu í apó­tek í vik­unni. Þar fékk hún þau svör að lyfið væri hvergi til og kæmi ekki a.m.k. næstu tvær vik­urn­ar.','bubbi@mbl.is','tint.jpg']]
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

#run()
run(host='0.0.0.0', port=os.environ.get('PORT'))
