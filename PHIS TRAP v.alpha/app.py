import flask
from flask import Flask, render_template, request
import joblib
import inputScript
import regex
import sys
import logging


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('home.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/predict', methods = ['POST'])
def make_prediction():
    LogisticRegression = joblib.load(r'D:\college\Nalaya thiran\PHIS TRAP v.alpha\model\Phishing_website.pkl', 'rb')
    if request.method=='POST':
        url = request.form['url']
        if not url:
            return render_template('home.html', label = 'Please input url')
        elif(not(regex.search(r'^(http|ftp)s?://', url))):
            return render_template('home.html', label = 'Please input full url, for exp- https://facebook.com')
        
        
        checkprediction = inputScript.main(url)
        prediction = LogisticRegression.predict(checkprediction)

        if prediction[0]==1 :
            label = 'website is not legitimate'
        elif prediction[0]==-1:
            label ='website is legitimate'
        
        return render_template('home.html', label=label)
        
        
if __name__ == '__main__':
    LogisticRegression = joblib.load(r'D:\college\Nalaya thiran\PHIS TRAP v.alpha\model\Phishing_website.pkl', 'rb')
    app.run()