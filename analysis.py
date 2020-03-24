from flask import Flask , render_template, request, Blueprint, redirect, url_for, flash
from flask import *
import pandas as pd
import io
import csv
import os
from werkzeug.utils import secure_filename
from tqdm import tqdm
from textblob import TextBlob
#from cleantext import clean


app = Flask(__name__)


global sentiment_textblob
sentiment_textblob=''

# Get the polarity score using below function
def get_textBlob_score(sent):
    # This polarity score is between -1 to 1
    polarity = TextBlob(sent).sentiment.polarity
    return polarity


@app.route('/')
def load():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sentiment():
    if request.method == 'POST':
        data= request.form['sampletext']
        # print('data:',data)
        #for i in range(len(data)):
        # sent=data['CleanText'][i]
        # print(sent)
        polarity=get_textBlob_score(data)
        # print('polarity:',polarity)
        if polarity > 0:
           sentiment_textblob = 'The sentiment for input text is positive'
        elif polarity < 0:
            sentiment_textblob = 'The sentiment for input text is negative'
        else:
            sentiment_textblob = 'The sentiment for input text is neutral'
    return render_template('index.html', result=sentiment_textblob)

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0', port=8080 )