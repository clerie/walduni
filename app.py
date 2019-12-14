#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def tu_ilmenau():
    return redirect("https://www.tu-ilmenau.de/", code=302)

@app.route('/about')
def about():
    return redirect("https://github.com/clerie/walduni", code=302)

@app.route('/turm/')
def turm():
    return redirect("https://turm.rz.tu-ilmenau.de/eE/aktuell/lstr_browser.php", code=302)

@app.route('/modultafeln/<course>/')
@app.route('/modultafel/<course>/')
@app.route('/modulplan/<course>/')
@app.route('/module/<course>/')
@app.route('/modultafeln/')
@app.route('/modultafel/')
@app.route('/modulplan/')
@app.route('/module/')
def modultafeln(course=""):
    courseToPath = {
        "amw": "AngewandteMedienundKommunikationswissenschaft/Bachelor/2014",
        "amk": "AngewandteMedienundKommunikationswissenschaft/Bachelor/2014",
        "bmt": "BiomedizinischeTechnik/Bachelor/2014/",
        "btc": "BiotechnischeChemie/Bachelor/2013/",
        "eit": "ElektrotechnikundInformationstechnik/Bachelor/2013/",
        "ft": "Fahrzeugtechnik/Bachelor/2013/",
        "in": "Informatik/Bachelor/2013/",
        "ii": "Ingenieurinformatik/Bachelor/2013/",
        "mb": "Maschinenbau/Bachelor/2013/",
        "mathe": "Mathematik/Bachelor/2013/",
        "mechatronik": "Mechatronik/Bachelor/2013/",
        "mt": "Medientechnologie/Bachelor/2013/",
        "mw": "Medienwirtschaft/Bachelor/2015/",
        "oso": "OptischeSystemtechnikOptronik/Bachelor/2013/",
        "tks": "TechnischeKybernetikundSystemtheorie/Bachelor/2013/",
        "physik": "TechnischePhysik/Bachelor/2013/",
        "ww": "Werkstoffwissenschaft/Bachelor/2013/",
        "wi": "Wirtschaftsinformatik/Bachelor/2015/",
        "wiw": "Wirtschaftsingenieurwesen/Bachelor/2015/?vertiefung=MB"
    }
    
    return redirect("https://www.tu-ilmenau.de/modultafeln/" + courseToPath.get(course, ""), code=302)

@app.route('/mail/')
@app.route('/webmail/')
def mail():
    return redirect("https://webmail.tu-ilmenau.de/", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
