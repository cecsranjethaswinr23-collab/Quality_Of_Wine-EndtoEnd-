from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd

# this must import from the prediction.py to run the app.py
from Quality_of_Wine.pipeline.prediction import PredictionPipeline


app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template("index.html")






if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)