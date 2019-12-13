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

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
