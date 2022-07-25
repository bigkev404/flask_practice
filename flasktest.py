# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:11:11 2022

@author: kevin
"""

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

list_names = ["kev","ash","kvothe"]

@app.route("/")
def home(): 
    return render_template("index.html", content=list_names)


if __name__ == "__main__": 
    app.run()
    

    

