# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import pickle
import numpy as np
import sklearn
import pandas as pd


app = Flask(__name__)

@app.route('/', methods = ["GET"])

def home():
    return render_template("home.html")


@app.route('/predict', methods = ["POST", "GET"])

def predict():
    if request.method == "POST":
        
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
                
        sex = request.form['sex']
        if (sex == 'male'):
            sex = 1
        else:
            sex = 0
            
        smoker = request.form['smoker']
        if (smoker == 'yes'):
            smoker = 1
        else:
            smoker = 0
            
        region = request.form['region']
        #region_northeast = 0
        if (region == 'region_northwest'):
            region_northwest = 1
            region_southeast = 0
            region_southwest = 0
        elif (region == 'region_southeast'):
            region_northwest = 0
            region_southeast = 1
            region_southwest = 0
        elif (region == 'region_southwest'):
            region_northwest = 0
            region_southeast = 0
            region_southwest = 1
        else:
            region_northwest = 0
            region_southeast = 0
            region_southwest = 0
            
        
        model = pickle.load(open("rf_regression.pkl", "rb"))
        
        prediction = model.predict([[age, sex, bmi, children, smoker, 
                                     region_northwest, region_southeast, region_southwest]])
        
        output = round(prediction[0], 2)
        
        return render_template('home.html', prediction_text="Your insurance premium is {}".format(output))
    

    return render_template("home.html")

    
if __name__ == "__main__":
    app.run(debug = True)

        

    
    
    
    
    
           