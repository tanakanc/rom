# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:18:29 2019

@author: tanakanc
""" 
#%%
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')
import numpy as np
import pandas as pd



   
@app.route('/home')
def home():
    monster = pd.read_csv("monster_table.csv")
    monstername = monster['name'].tolist()  
    monstername.sort()
    return render_template('home.html',monstername=monstername)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   monster = pd.read_csv("monster_table.csv")
   monster['namelower']= monster['name'].str.lower()
   
   if request.method == 'POST':
      result = request.form
      serchresult= monster[monster['namelower'].str.contains(result['Monster name'].lower())]
      if len(serchresult)== 0:
       serchresult1  = []
      else:   
       serchresult1=serchresult.iloc[0,0:6]
      length_search= len(serchresult1)
      
      return render_template("result.html",result = result,serchresult=serchresult,serchresult1=serchresult1,length_search=length_search)

if __name__ == '__main__':
    app.run()
    
#if __name__=='__main__':
#    app.run(port=5000,debug = True)

    
