#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask,redirect
from bs4 import BeautifulSoup
import requests
from datetime import date

app = Flask(__name__)

@app.route('/')
def tu_ilmenau():
    return redirect("https://www.tu-ilmenau.de/", code=302)

@app.route('/about/')
def about():
    return redirect("https://git.clerie.de/clerie/walduni", code=302)

@app.route('/turm/')
def turm():
    return redirect("https://turm.rz.tu-ilmenau.de/eE/aktuell/lstr_browser.php", code=302)

 @app.route('/moodle/')
 def moodle():
     return redirect("https://moodle2.tu-ilmenau.de/", code=302)

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

@app.route('/unirz/')
@app.route('/rz/')
@app.route('/1111/')
@app.route('/elfelf/')
def unirz():
    return redirect("https://www.tu-ilmenau.de/unirz/", code=302)

@app.route('/unibib/')
@app.route('/bib/')
def ub():
    return redirect("https://www.tu-ilmenau.de/ub/", code=302)

@app.route('/vlv/')
def vlv():
    return redirect("https://www.tu-ilmenau.de/vlv/index.php?id=330", code=302)

########################################################################################################################
# FeM
########################################################################################################################

# FeM
@app.route('/fem/')
def fem():
    return redirect("https://www.fem.tu-ilmenau.de/aktuelles/", code=302)

########################################################################################################################
# ILSC
########################################################################################################################

# ILSC
@app.route('/ilsc/')
def ilsc():
    return redirect("https://www.tu-ilmenau.de/fsr-mn/", code=302)

# BC
@app.route('/bc/')
def bc_club():
    return redirect("https://www.bc-club.de/", code=302)

# BD
@app.route('/bd/')
def bd_club():
    return redirect("http://www.bd-club.de/", code=302)

# BH
@app.route('/bh/')
def bh_club():
    return redirect("http://bh-club.de/", code=302)

# BI
@app.route('/bi/')
def bi_club():
    return redirect("https://www.bi-club.de/", code=302)

# Montagsküche
@app.route('/montag/')
def montagskueche():
    # Get the startpage of bi club
    try:
        current_event = requests.get("https://www.bi-club.de/")
        current_soup = BeautifulSoup(current_event.text, 'html.parser')
        # Get an array of all events
        events = current_soup.find(id='main').div.div.div.div.div.div.div.div.find_all('div', recursive=False)
    except:
        return redirect("https://www.bi-club.de/tags/montagskueche", code=302)

    # Pseudo event
    next_montagskueche = date.max
    next_montagskueche_url = ""

    for event in events:
        # Get interesting information
        content = event.div.div.div.div.find_all('div', recursive=False)[1]
        # Get title
        title = content.h2.a.text
        # Get date
        date_string = content.div.div.span.text.split(' - ')[1].split('.')
        date_object = date(int(date_string[2]), int(date_string[1]), int(date_string[0]))
        # Get url
        url = content.h2.a.get('href')

        # Select the event
        if "Montagsküche" in title and date_object >= date.today() and date_object < next_montagskueche:
            next_montagskueche = date_object
            next_montagskueche_url = url

    # Answer
    if next_montagskueche_url != "":
        return redirect(next_montagskueche_url, code=302)
    else:
        return redirect("https://www.bi-club.de/tags/montagskueche", code=302)

########################################################################################################################
# Stura
########################################################################################################################

# Stura
@app.route('/stura/')
def stura():
    return redirect("https://stura.tu-ilmenau.de/", code=302)

# FSR EI
@app.route('/ei/')
@app.route('/fsr-ei/')
def fsr_ei():
    return redirect("https://www.tu-ilmenau.de/fachschaftsrat-ei/", code=302)

# FSR IA
@app.route('/ia/')
@app.route('/fsr-ia/')
def fsr_ia():
    return redirect("https://www.tu-ilmenau.de/fsr-ia/", code=302)

# FSR MB
@app.route('/mb/')
@app.route('/fsr-mb/')
def fsr_mb():
    return redirect("https://www.tu-ilmenau.de/fsr-mb/", code=302)

# FSR MN
@app.route('/mn/')
@app.route('/fsr-mn/')
def fsr_mn():
    return redirect("https://www.tu-ilmenau.de/fsr-mn/", code=302)

########################################################################################################################
# StuWe
########################################################################################################################

@app.route('/mensa/')
def mensa():
    return redirect("https://spi.tu-ilmenau.de/mensa", code=302)

@app.route('/block/a/')
def block_a():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-7haus-a.html", code=302)

@app.route('/block/b/')
def block_b():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-9-haus-b.html", code=302)

@app.route('/block/c/')
def block_c():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-16-haus-c.html", code=302)

@app.route('/block/d/')
def block_d():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-18-haus-d.html", code=302)

@app.route('/block/e/')
def block_e():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-10-haus-e.html", code=302)

@app.route('/block/h/')
def block_h():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-2-haus-h.html", code=302)

@app.route('/block/i/')
def block_i():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-4-haus-i.html", code=302)

@app.route('/block/k/')
def block_k():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/am-helmholtzring-2-4-haus-k.html", code=302)

@app.route('/block/l/')
def block_l():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/max-planck-ring-6-8-haus-l.html", code=302)

@app.route('/block/n/')
def block_n():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/am-helmholtzring-3-haus-n.html", code=302)

@app.route('/block/p/')
def block_p():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/ehrenbergstrasse-37-haus-p.html", code=302)

@app.route('/block/q/')
def block_q():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/am-ehrenberg-6-haus-q.html", code=302)

@app.route('/block/z/')
def block_z():
    return redirect("https://www.stw-thueringen.de/deutsch/wohnen/wohnanlagen/ilmenau/goetheallee-11-haus-zapf.html", code=302)

@app.route('/block/cjd/')
def block_cjd():
    return ""

@app.route('/block/pp/')
@app.route('/block/prophis/')
def block_pp():
    return ""

@app.route('/bahn/')
@app.route('/bahnhof/')
@app.route('/fahrplan/')
def bahn():
    return redirect("https://marudor.de/Ilmenau", code=302)


########################################################################################################################
# Base
########################################################################################################################

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
