from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd

# this must import from the prediction.py to run the app.py
from Quality_of_Wine.pipeline.prediction import PredictionPipeline


